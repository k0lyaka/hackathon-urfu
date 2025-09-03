import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ApiContext } from "@/contexts/ApiContext";
import type { Specialization } from "@/lib/api";
import { ArrowLeft, Star, TrendingUp, Users } from "lucide-react";
import { useContext, useEffect, useState } from "react";

function Specializations() {
  const [specializations, setSpecializations] = useState<Specialization[]>([]);
  const api = useContext(ApiContext);

  useEffect(() => {
    if (!api.client) return;

    api.client.getSpecializations().then((data) => {
      setSpecializations(data);
    });
  }, [api.client]);

  return (
    <div className="min-h-screen bg-background p-4">
      <div className="max-w-2xl mx-auto">
        {/* Header */}
        <div className="mb-6">
          <div>
            <Button
              variant="ghost"
              size="sm"
              className="flex items-center gap-2"
            >
              <ArrowLeft />
              Отредактировать анкету
            </Button>
          </div>
          <div>
            <h1 className="text-2xl font-bold text-wrap">
              Специальности ИРИТ-РТФ
            </h1>
            <p className="text-sm text-muted-foreground">
              Выберите направление обучения
            </p>
          </div>
        </div>

        {/* Specialties List */}
        <div className="space-y-4">
          {specializations.map((specialty, index) => (
            <Card
              key={specialty.id}
              className={`relative transition-all hover:shadow-lg ${
                index === 0
                  ? "border-primary bg-gradient-to-r from-primary/5 to-transparent"
                  : ""
              }`}
            >
              {index === 0 && (
                <div className="absolute -top-2 -right-2">
                  <Badge className="bg-primary text-primary-foreground flex items-center gap-1 px-3 py-1">
                    <Star className="w-3 h-3 fill-current" />
                    Лучший выбор
                  </Badge>
                </div>
              )}

              <CardHeader className="pb-3">
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <CardTitle className="text-lg mb-1 text-balance">
                      {specialty.name}
                    </CardTitle>
                    <p className="text-sm text-muted-foreground mb-2">
                      Код: {specialty.code}
                    </p>
                  </div>
                </div>
              </CardHeader>

              <CardContent className="pt-0">
                {/* Stats */}
                <div className="flex items-center justify-between mb-4 text-sm text-muted-foreground">
                  <div className="flex items-center gap-1">
                    <Users className="w-4 h-4" />
                    {specialty.scores[0].seats} мест
                  </div>
                  <div className="flex items-center gap-1">
                    <TrendingUp className="w-4 h-4" />
                    от {specialty.scores[0].minimal_score} баллов
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Footer Info */}
        <div className="mt-8 p-4 bg-muted/30 rounded-lg">
          <p className="text-sm text-muted-foreground text-center">
            Институт радиоэлектроники и информационных технологий - РТФ
            <br />
            Уральский федеральный университет
          </p>
        </div>
      </div>
    </div>
  );
}

export default Specializations;
