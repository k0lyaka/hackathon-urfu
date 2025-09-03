import ProgressBar from "@/components/progress-bar";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { ApiContext } from "@/contexts/ApiContext";

import { ArrowLeft, ArrowRight, CheckCircle } from "lucide-react";
import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

interface FormData {
  subjects: {
    math: number | null;
    russian: number | null;
    additional: string;
    additionalScore: number | null;
  };
  interests: string;
}

const additionalSubjects = {
  computer_science: "Информатика",
  physics: "Физика",
};

const currentYear = new Date().getFullYear();

function Form() {
  const [isLoading, setIsLoading] = useState(false);
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState<FormData>({
    subjects: {
      math: null,
      russian: null,
      additional: "",
      additionalScore: null,
    },
    interests: "",
  });

  const api = useContext(ApiContext);

  const navigate = useNavigate();

  useEffect(() => {
    if (!api.client) return;

    api.client.getProfile().then((data) => {
      const additional = data.exam_scores.find(
        (score) => !["math", "russian"].includes(score.subject)
      );

      setFormData((old) => ({
        subjects: {
          math:
            data.exam_scores.find((score) => score.subject === "math")?.score ??
            null,
          russian:
            data.exam_scores.find((score) => score.subject === "russian")
              ?.score ?? null,
          additional: additional?.subject ?? "",
          additionalScore: additional?.score ?? null,
        },
        interests: data.full_interest_text || old.interests,
      }));
    });
  }, [api]);

  const totalSteps = 2;

  const handleNext = () => {
    if (currentStep === 1) {
      void api.client!.addExamScores({
        exams: [
          {
            year: currentYear,
            subject: "math",
            score: formData.subjects.math!,
          },
          {
            year: currentYear,
            subject: "russian",
            score: formData.subjects.russian!,
          },
          {
            year: currentYear,
            subject: formData.subjects
              .additional as keyof typeof additionalSubjects,
            score: formData.subjects.additionalScore!,
          },
        ],
      });
    }

    if (currentStep < totalSteps) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handleBack = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  const isStepValid = () => {
    switch (currentStep) {
      case 1:
        return (
          formData.subjects.math !== null &&
          formData.subjects.russian !== null &&
          formData.subjects.additional !== "" &&
          formData.subjects.additionalScore !== null
        );
      case 2:
        return formData.interests.length > 0;
      case 3:
        return true;
      default:
        return false;
    }
  };

  const handleSubjectScoreChange = (
    subject: keyof FormData["subjects"],
    value: string
  ) => {
    const numValue = value === "" ? null : Number.parseInt(value);
    setFormData((prev) => ({
      ...prev,
      subjects: {
        ...prev.subjects,
        [subject]: numValue,
      },
    }));
  };

  const handleSubmit = () => {
    setIsLoading(true);
    api
      .client!.updateInterests({ interests: formData.interests })
      .then(() => {
        navigate("/specializations");
      })
      .catch(() => setIsLoading(false));
  };

  return (
    <div className="min-h-screen bg-background p-4 h-screen">
      <div className="max-w-md mx-auto space-y-2">
        {formData.interests &&
          formData.subjects.math &&
          formData.subjects.russian &&
          formData.subjects.additionalScore && (
            <Button
              variant="ghost"
              size="sm"
              className="flex items-center gap-2"
              onClick={() => navigate("/specializations")}
            >
              <ArrowRight />
              Специальности
            </Button>
          )}
        <ProgressBar currentStep={currentStep} totalSteps={totalSteps} />
      </div>

      {currentStep === 1 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-center">Предметы и баллы ЕГЭ</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            {/* Math Score */}
            <div className="space-y-2">
              <Label htmlFor="math">Математика (обязательный)</Label>
              <Input
                id="math"
                type="number"
                min="0"
                max="100"
                placeholder="Введите баллы"
                value={formData.subjects.math || ""}
                onChange={(e) =>
                  handleSubjectScoreChange("math", e.target.value)
                }
              />
            </div>

            {/* Russian Score */}
            <div className="space-y-2">
              <Label htmlFor="russian">Русский язык (обязательный)</Label>
              <Input
                id="russian"
                type="number"
                min="0"
                max="100"
                placeholder="Введите баллы"
                value={formData.subjects.russian || ""}
                onChange={(e) =>
                  handleSubjectScoreChange("russian", e.target.value)
                }
              />
            </div>

            {/* Additional Subject */}
            <div className="space-y-2">
              <Label>Дополнительный предмет</Label>
              <Select
                value={formData.subjects.additional}
                onValueChange={(value) =>
                  setFormData((prev) => ({
                    ...prev,
                    subjects: { ...prev.subjects, additional: value },
                  }))
                }
              >
                <SelectTrigger>
                  <SelectValue placeholder="Выберите предмет" />
                </SelectTrigger>
                <SelectContent>
                  {Object.entries(additionalSubjects).map(([key, value]) => (
                    <SelectItem key={key} value={key}>
                      {value}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            {/* Additional Subject Score */}
            {formData.subjects.additional && (
              <div className="space-y-2">
                <Label htmlFor="additional-score">
                  {
                    additionalSubjects[
                      formData.subjects
                        .additional as keyof typeof additionalSubjects
                    ]
                  }
                </Label>
                <Input
                  id="additional-score"
                  type="number"
                  min="0"
                  max="100"
                  placeholder="Введите баллы"
                  value={formData.subjects.additionalScore || ""}
                  onChange={(e) =>
                    handleSubjectScoreChange("additionalScore", e.target.value)
                  }
                />
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {currentStep === 2 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-center">Пожелания</CardTitle>
            <p className="text-sm text-muted-foreground text-center">
              Расскажите о своих пожеланиях и дополнительной информации
            </p>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="wishes">Ваши пожелания</Label>
                <Textarea
                  id="wishes"
                  placeholder="Расскажите о своих целях, интересах или вопросах..."
                  value={formData.interests}
                  disabled={isLoading}
                  onChange={(e) =>
                    setFormData((prev) => ({
                      ...prev,
                      interests: e.target.value,
                    }))
                  }
                  rows={4}
                />
              </div>

              {/* Summary */}
              <div className="mt-6 p-4 bg-muted rounded-lg">
                <h3 className="font-semibold mb-2">Сводка данных:</h3>
                <div className="text-sm space-y-1">
                  <p>Математика: {formData.subjects.math} баллов</p>
                  <p>Русский язык: {formData.subjects.russian} баллов</p>
                  <p>
                    {
                      additionalSubjects[
                        formData.subjects
                          .additional as keyof typeof additionalSubjects
                      ]
                    }
                    : {formData.subjects.additionalScore} баллов
                  </p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      <div className="flex justify-between mt-6">
        <Button
          variant="outline"
          onClick={handleBack}
          disabled={currentStep === 1 || isLoading}
          className="flex items-center gap-2 bg-transparent"
        >
          <ArrowLeft className="w-4 h-4" />
          Назад
        </Button>

        {currentStep < totalSteps ? (
          <Button
            onClick={handleNext}
            disabled={!isStepValid() || isLoading}
            className="flex items-center gap-2"
          >
            Далее
            <ArrowRight className="w-4 h-4" />
          </Button>
        ) : (
          <Button
            onClick={handleSubmit}
            className="flex items-center gap-2"
            disabled={isLoading}
          >
            <CheckCircle className="w-4 h-4" />
            Отправить
          </Button>
        )}
      </div>
    </div>
  );
}

export default Form;
