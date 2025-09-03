"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
import { Progress } from "@/components/ui/progress"
import { ChevronLeft, ChevronRight, Check, GraduationCap, AlertCircle } from "lucide-react"

interface EgeScores {
    russian: number
    math: number
    elective: string
    electiveScore: number
}

interface RegistrationData {
    egeScores: EgeScores
    preferences: string
}

interface ValidationErrors {
    russian?: string
    math?: string
    electiveScore?: string
}

export default function RegistrationPage() {
    const [currentStep, setCurrentStep] = useState(1)
    const [registrationData, setRegistrationData] = useState<RegistrationData>({
        egeScores: {
            russian: 0,
            math: 0,
            elective: "",
            electiveScore: 0,
        },
        preferences: "",
    })

    const [validationErrors, setValidationErrors] = useState<ValidationErrors>({})

    const totalSteps = 3
    const progress = (currentStep / totalSteps) * 100

    const electiveSubjects = [
        { value: "physics", label: "Физика" },
        { value: "informatics", label: "Информатика" },
        { value: "chemistry", label: "Химия" },
        { value: "biology", label: "Биология" },
        { value: "history", label: "История" },
        { value: "social", label: "Обществознание" },
    ]

    const validateScore = (score: number, _field: keyof ValidationErrors): string | undefined => {
        if (score < 0 || score > 100) {
            return "Балл должен быть от 0 до 100"
        }
        if (score === 0) {
            return "Введите балл"
        }
        return undefined
    }

    const handleScoreChange = (field: keyof EgeScores, value: string) => {
        const numValue = Number.parseInt(value) || 0

        setRegistrationData((prev) => ({
            ...prev,
            egeScores: { ...prev.egeScores, [field]: numValue },
        }))

        if (field === "russian" || field === "math" || field === "electiveScore") {
            const error = validateScore(numValue, field as keyof ValidationErrors)
            setValidationErrors((prev) => ({
                ...prev,
                [field]: error,
            }))
        }
    }

    const handleNext = () => {
        if (currentStep < totalSteps) {
            setCurrentStep(currentStep + 1)
        }
    }

    const handlePrevious = () => {
        if (currentStep > 1) {
            setCurrentStep(currentStep - 1)
        }
    }

    const handleSubmit = () => {
        console.log("Регистрация завершена:", registrationData)
        alert('Регистрация успешно завершена!')
        window.location.href = "/directions"

    }

    const isStep1Valid = () => {
        const hasErrors = Object.values(validationErrors).some((error) => error !== undefined)
        const hasAllScores =
            registrationData.egeScores.russian > 0 &&
            registrationData.egeScores.math > 0 &&
            registrationData.egeScores.elective &&
            registrationData.egeScores.electiveScore > 0

        return !hasErrors && hasAllScores
    }

    return (
        <div className="bg-background p-2 sm:p-4 min-h-screen sm:min-h-0">
            <div className="w-full max-w-xs xs:max-w-sm sm:max-w-md mx-auto">
                {/* Header */}
                <div className="text-center mb-3 sm:mb-4">
                    <div className="flex items-center justify-center gap-2 mb-1 sm:mb-2">
                        <div className="w-6 h-6 sm:w-8 sm:h-8 bg-primary rounded-full flex items-center justify-center">
                            <GraduationCap className="w-3 h-3 sm:w-4 sm:h-4 text-primary-foreground" />
                        </div>
                        <h1 className="text-lg sm:text-xl font-bold text-foreground">УрФУ</h1>
                    </div>
                    <h2 className="text-xs sm:text-sm text-muted-foreground">Регистрация абитуриента</h2>
                </div>

                {/* Progress Bar */}
                <div className="mb-3 sm:mb-4">
                    <div className="flex justify-between text-xs text-muted-foreground mb-1 sm:mb-2">
            <span>
              Шаг {currentStep} из {totalSteps}
            </span>
                        <span>{Math.round(progress)}%</span>
                    </div>
                    <Progress value={progress} className="h-1 sm:h-1.5" />
                </div>

                {/* Step Content */}
                <Card>
                    <CardHeader className="pb-2 sm:pb-3 px-3 sm:px-6 pt-3 sm:pt-6">
                        <CardTitle className="text-center text-base sm:text-lg">
                            {currentStep === 1 && "Баллы ЕГЭ"}
                            {currentStep === 2 && "Пожелания к учебе"}
                            {currentStep === 3 && "Подтверждение данных"}
                        </CardTitle>
                        <CardDescription className="text-center text-xs leading-tight">
                            {currentStep === 1 && "Введите ваши результаты единого государственного экзамена"}
                            {currentStep === 2 && "Расскажите о ваших предпочтениях и целях в обучении"}
                            {currentStep === 3 && "Проверьте введенные данные перед отправкой"}
                        </CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-3 sm:space-y-4 pt-0 px-3 sm:px-6 pb-3 sm:pb-6">
                        {/* Step 1: EGE Scores */}
                        {currentStep === 1 && (
                            <div className="space-y-3 sm:space-y-4">
                                {/* Russian Language */}
                                <div className="space-y-1.5 sm:space-y-2">
                                    <Label className="text-xs font-medium">Русский язык (обязательный)</Label>
                                    <div className="flex gap-1.5 sm:gap-2">
                                        <div className="flex flex-col">
                                            <Input
                                                type="number"
                                                min="0"
                                                max="100"
                                                placeholder="Баллы"
                                                value={registrationData.egeScores.russian || ""}
                                                onChange={(e) => handleScoreChange("russian", e.target.value)}
                                                className={`sm:w-20 h-8 sm:h-9 text-xs sm:text-sm w-20 ${
                                                    validationErrors.russian ? "border-destructive" : ""
                                                }`}
                                            />
                                        </div>
                                    </div>
                                    {validationErrors.russian && (
                                        <div className="flex items-center gap-1 text-destructive">
                                            <AlertCircle className="w-3 h-3" />
                                            <span className="text-xs">{validationErrors.russian}</span>
                                        </div>
                                    )}
                                </div>

                                {/* Mathematics */}
                                <div className="space-y-1.5 sm:space-y-2">
                                    <Label className="text-xs font-medium">Математика (профильный уровень)</Label>
                                    <div className="flex gap-1.5 sm:gap-2">
                                        <div className="flex flex-col">
                                            <Input
                                                type="number"
                                                min="0"
                                                max="100"
                                                placeholder="Баллы"
                                                value={registrationData.egeScores.math || ""}
                                                onChange={(e) => handleScoreChange("math", e.target.value)}
                                                className={`sm:w-20 h-8 sm:h-9 text-xs sm:text-sm w-20 ${
                                                    validationErrors.math ? "border-destructive" : ""
                                                }`}
                                            />
                                        </div>
                                    </div>
                                    {validationErrors.math && (
                                        <div className="flex items-center gap-1 text-destructive">
                                            <AlertCircle className="w-3 h-3" />
                                            <span className="text-xs">{validationErrors.math}</span>
                                        </div>
                                    )}
                                </div>

                                {/* Elective Subject */}
                                <div className="space-y-1.5 sm:space-y-2">
                                    <Label className="text-xs font-medium">Предмет по выбору</Label>
                                    <div className="flex gap-1.5 sm:gap-2">
                                        <Select
                                            value={registrationData.egeScores.elective}
                                            onValueChange={(value) =>
                                                setRegistrationData((prev) => ({
                                                    ...prev,
                                                    egeScores: { ...prev.egeScores, elective: value },
                                                }))
                                            }
                                        >
                                            <SelectTrigger className="h-8 sm:h-9 text-xs sm:text-sm">
                                                <SelectValue placeholder="Выберите предмет" />
                                            </SelectTrigger>
                                            <SelectContent>
                                                {electiveSubjects.map((subject) => (
                                                    <SelectItem key={subject.value} value={subject.value}>
                                                        {subject.label}
                                                    </SelectItem>
                                                ))}
                                            </SelectContent>
                                        </Select>
                                        <div className="flex flex-col">
                                            <Input
                                                type="number"
                                                min="0"
                                                max="100"
                                                placeholder="Баллы"
                                                value={registrationData.egeScores.electiveScore || ""}
                                                onChange={(e) => handleScoreChange("electiveScore", e.target.value)}
                                                className={`sm:w-20 h-8 sm:h-9 text-xs sm:text-sm w-20 ${
                                                    validationErrors.electiveScore ? "border-destructive" : ""
                                                }`}
                                            />
                                        </div>
                                    </div>
                                    {validationErrors.electiveScore && (
                                        <div className="flex items-center gap-1 text-destructive">
                                            <AlertCircle className="w-3 h-3" />
                                            <span className="text-xs">{validationErrors.electiveScore}</span>
                                        </div>
                                    )}
                                </div>

                                <div className="bg-muted p-2 sm:p-3 rounded-lg">
                                    <p className="text-xs text-muted-foreground leading-tight">
                                        <strong>Важно:</strong> Баллы ЕГЭ должны быть от 0 до 100. Убедитесь, что введенные баллы
                                        соответствуют вашим официальным результатам ЕГЭ.
                                    </p>
                                </div>
                            </div>
                        )}

                        {/* Step 2: Preferences */}
                        {currentStep === 2 && (
                            <div className="space-y-3 sm:space-y-4">
                                <div>
                                    <Label htmlFor="preferences" className="text-xs font-medium">
                                        Ваши пожелания и цели в обучении
                                    </Label>
                                    <Textarea
                                        id="preferences"
                                        placeholder="Расскажите о ваших интересах, предпочтениях по форме обучения, планах на будущее..."
                                        value={registrationData.preferences}
                                        onChange={(e) =>
                                            setRegistrationData((prev) => ({
                                                ...prev,
                                                preferences: e.target.value,
                                            }))
                                        }
                                        className="mt-1.5 sm:mt-2 min-h-[60px] sm:min-h-[80px] text-xs sm:text-sm"
                                    />
                                </div>

                                <div className="bg-muted p-2 sm:p-3 rounded-lg">
                                    <p className="text-xs text-muted-foreground leading-tight">
                                        <strong>Подсказка:</strong> Эта информация поможет нам лучше понять ваши потребности.
                                    </p>
                                </div>
                            </div>
                        )}

                        {/* Step 3: Confirmation */}
                        {currentStep === 3 && (
                            <div className="space-y-3 sm:space-y-4">
                                <div className="space-y-2 sm:space-y-3">
                                    <div>
                                        <h3 className="font-semibold text-xs sm:text-sm mb-1.5 sm:mb-2">Баллы ЕГЭ</h3>
                                        <div className="grid gap-0.5 sm:gap-1 text-xs">
                                            <div className="flex justify-between">
                                                <span>Русский язык:</span>
                                                <span className="font-medium">{registrationData.egeScores.russian} баллов</span>
                                            </div>
                                            <div className="flex justify-between">
                                                <span>Математика (профиль):</span>
                                                <span className="font-medium">{registrationData.egeScores.math} баллов</span>
                                            </div>
                                            <div className="flex justify-between">
                        <span>
                          {electiveSubjects.find((s) => s.value === registrationData.egeScores.elective)?.label}:
                        </span>
                                                <span className="font-medium">{registrationData.egeScores.electiveScore} баллов</span>
                                            </div>
                                            <div className="border-t pt-1 mt-1.5 sm:mt-2">
                                                <div className="flex justify-between font-semibold">
                                                    <span>Общий балл:</span>
                                                    <span className="text-primary">
                            {registrationData.egeScores.russian +
                                registrationData.egeScores.math +
                                registrationData.egeScores.electiveScore}{" "}
                                                        баллов
                          </span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    {registrationData.preferences && (
                                        <div>
                                            <h3 className="font-semibold text-xs sm:text-sm mb-1.5 sm:mb-2">Пожелания к учебе</h3>
                                            <p className="text-xs text-muted-foreground bg-muted p-2 rounded leading-tight">
                                                {registrationData.preferences}
                                            </p>
                                        </div>
                                    )}
                                </div>

                                <div className="bg-accent/10 border border-accent/20 p-2 sm:p-3 rounded-lg">
                                    <p className="text-xs text-accent-foreground leading-tight">
                                        <strong>Внимание:</strong> После подтверждения данные будут отправлены в приемную комиссию УрФУ.
                                    </p>
                                </div>
                            </div>
                        )}
                    </CardContent>
                </Card>

                {/* Navigation Buttons */}
                <div className="flex justify-between mt-3 sm:mt-4 gap-2">
                    <Button
                        variant="outline"
                        onClick={handlePrevious}
                        disabled={currentStep === 1}
                        className="flex items-center gap-1 bg-transparent h-8 sm:h-9 text-xs sm:text-sm px-3 sm:px-4"
                    >
                        <ChevronLeft className="w-3 h-3" />
                        Назад
                    </Button>

                    {currentStep < totalSteps ? (
                        <Button
                            onClick={handleNext}
                            disabled={currentStep === 1 && !isStep1Valid()}
                            className="flex items-center gap-1 h-8 sm:h-9 text-xs sm:text-sm px-3 sm:px-4"
                        >
                            Далее
                            <ChevronRight className="w-3 h-3" />
                        </Button>
                    ) : (
                        <Button
                            onClick={handleSubmit}
                            className="flex items-center gap-1 bg-primary hover:bg-primary/90 h-8 sm:h-9 text-xs sm:text-sm px-3 sm:px-4"
                        >
                            <Check className="w-3 h-3" />
                            Подтвердить
                        </Button>
                    )}
                </div>
            </div>
        </div>
    )
}
