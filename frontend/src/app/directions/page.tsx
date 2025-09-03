"use client"

import { useState, useEffect } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { GraduationCap, Search, Filter, Users, Clock, TrendingUp, ChevronLeft, Star, MapPin } from "lucide-react"

interface Direction {
    id: string
    name: string
    code: string
    faculty: string
    minScore: number
    duration: number
    places: number
    category: string
    description: string
    subjects: string[]
    employment: string[]
    isPopular?: boolean
}

const directions: Direction[] = [
    {
        id: "1",
        name: "Программная инженерия",
        code: "09.03.04",
        faculty: "ИнЭО",
        minScore: 240,
        duration: 4,
        places: 120,
        category: "Информационные технологии",
        description: "Разработка программного обеспечения, мобильных приложений и веб-систем",
        subjects: ["Русский язык", "Математика", "Информатика"],
        employment: ["Программист", "Разработчик", "Архитектор ПО"],
        isPopular: true,
    },
    {
        id: "2",
        name: "Информационные системы и технологии",
        code: "09.03.02",
        faculty: "ИнЭО",
        minScore: 220,
        duration: 4,
        places: 100,
        category: "Информационные технологии",
        description: "Проектирование и администрирование информационных систем",
        subjects: ["Русский язык", "Математика", "Информатика"],
        employment: ["Системный администратор", "Аналитик", "IT-консультант"],
    },
    {
        id: "3",
        name: "Прикладная математика и информатика",
        code: "01.03.02",
        faculty: "ИММт",
        minScore: 250,
        duration: 4,
        places: 80,
        category: "Математика и информатика",
        description: "Mathematical modeling, data analysis and computational methods",
        subjects: ["Русский язык", "Математика", "Информатика"],
        employment: ["Data Scientist", "Аналитик данных", "Исследователь"],
        isPopular: true,
    },
    {
        id: "4",
        name: "Радиотехника",
        code: "11.03.01",
        faculty: "РтИ",
        minScore: 200,
        duration: 4,
        places: 90,
        category: "Техника и технологии",
        description: "Разработка радиоэлектронных устройств и систем связи",
        subjects: ["Русский язык", "Математика", "Физика"],
        employment: ["Инженер-радиотехник", "Разработчик устройств", "Системный инженер"],
    },
    {
        id: "5",
        name: "Машиностроение",
        code: "15.03.01",
        faculty: "МашИнст",
        minScore: 180,
        duration: 4,
        places: 110,
        category: "Техника и технологии",
        description: "Проектирование и производство машин и механизмов",
        subjects: ["Русский язык", "Математика", "Физика"],
        employment: ["Инженер-конструктор", "Технолог", "Менеджер производства"],
    },
    {
        id: "6",
        name: "Экономика",
        code: "38.03.01",
        faculty: "ВШЭиМ",
        minScore: 210,
        duration: 4,
        places: 150,
        category: "Экономика и управление",
        description: "Экономический анализ, финансовое планирование и управление",
        subjects: ["Русский язык", "Математика", "Обществознание"],
        employment: ["Экономист", "Финансовый аналитик", "Менеджер"],
    },
]

const categories = [
    "Все направления",
    "Информационные технологии",
    "Математика и информатика",
    "Техника и технологии",
    "Экономика и управление",
]

export default function DirectionsPage() {
    const [searchQuery, setSearchQuery] = useState("")
    const [selectedCategory, setSelectedCategory] = useState("Все направления")
    const [minScoreFilter, setMinScoreFilter] = useState("")
    const [filteredDirections, setFilteredDirections] = useState(directions)

    useEffect(() => {
        let filtered = directions

        if (searchQuery) {
            filtered = filtered.filter(
                (direction) =>
                    direction.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                    direction.faculty.toLowerCase().includes(searchQuery.toLowerCase()) ||
                    direction.code.includes(searchQuery),
            )
        }

        if (selectedCategory !== "Все направления") {
            filtered = filtered.filter((direction) => direction.category === selectedCategory)
        }

        if (minScoreFilter) {
            const userScore = Number.parseInt(minScoreFilter)
            filtered = filtered.filter((direction) => direction.minScore <= userScore)
        }

        setFilteredDirections(filtered)
    }, [searchQuery, selectedCategory, minScoreFilter])

    useEffect(() => {
        // @ts-expect-error: Telegram WebApp is not defined yet
        if (typeof window !== "undefined" && window.Telegram?.WebApp) {
            // @ts-expect-error: Telegram WebApp is not defined yet
            const tg = window.Telegram.WebApp
            tg.ready()
            tg.expand()
            tg.setHeaderColor("#ffffff")
            tg.setBackgroundColor("#ffffff")
            tg.disableVerticalSwipes()
        }
    }, [])

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
                    <h2 className="text-xs sm:text-sm text-muted-foreground">Направления подготовки</h2>
                </div>

                {/* Filters */}
                <Card className="mb-3 sm:mb-4">
                    <CardContent className="p-3 sm:p-4 space-y-2 sm:space-y-3">
                        {/* Search */}
                        <div className="relative">
                            <Search className="absolute left-2 top-1/2 transform -translate-y-1/2 w-3 h-3 text-muted-foreground" />
                            <Input
                                placeholder="Поиск направлений..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                className="pl-7 h-8 sm:h-9 text-xs sm:text-sm"
                            />
                        </div>

                        {/* Category Filter */}
                        <div className="flex gap-2">
                            <Select value={selectedCategory} onValueChange={setSelectedCategory}>
                                <SelectTrigger className="flex-1 h-8 sm:h-9 text-xs sm:text-sm">
                                    <Filter className="w-3 h-3 mr-1" />
                                    <SelectValue />
                                </SelectTrigger>
                                <SelectContent>
                                    {categories.map((category) => (
                                        <SelectItem key={category} value={category}>
                                            {category}
                                        </SelectItem>
                                    ))}
                                </SelectContent>
                            </Select>

                            <Input
                                type="number"
                                placeholder="Мин. балл"
                                value={minScoreFilter}
                                onChange={(e) => setMinScoreFilter(e.target.value)}
                                className="w-20 sm:w-24 h-8 sm:h-9 text-xs sm:text-sm"
                            />
                        </div>
                    </CardContent>
                </Card>

                {/* Results Count */}
                <div className="flex items-center justify-between mb-2 sm:mb-3">
                    <span className="text-xs text-muted-foreground">Найдено: {filteredDirections.length} направлений</span>
                    {filteredDirections.length > 0 && (
                        <span className="text-xs text-muted-foreground">Свайп для подробностей</span>
                    )}
                </div>

                {/* Directions List */}
                <div className="space-y-2 sm:space-y-3">
                    {filteredDirections.length === 0 ? (
                        <Card>
                            <CardContent className="p-4 text-center">
                                <p className="text-sm text-muted-foreground">Направления не найдены. Попробуйте изменить фильтры.</p>
                            </CardContent>
                        </Card>
                    ) : (
                        filteredDirections.map((direction) => (
                            <Card
                                key={direction.id}
                                className="cursor-pointer hover:shadow-md transition-shadow"
                            >
                                <CardHeader className="pb-2 px-3 sm:px-4 pt-3">
                                    <div className="flex items-start justify-between gap-2">
                                        <div className="flex-1 min-w-0">
                                            <div className="flex items-center gap-1 mb-1">
                                                {direction.isPopular && <Star className="w-3 h-3 text-yellow-500 fill-current" />}
                                                <CardTitle className="text-sm sm:text-base leading-tight">{direction.name}</CardTitle>
                                            </div>
                                            <div className="flex items-center gap-2 text-xs text-muted-foreground">
                                                <span>{direction.code}</span>
                                                <span>•</span>
                                                <div className="flex items-center gap-1">
                                                    <MapPin className="w-3 h-3" />
                                                    {direction.faculty}
                                                </div>
                                            </div>
                                        </div>
                                        <Badge
                                            variant={
                                                direction.minScore <= 200 ? "secondary" : direction.minScore <= 230 ? "default" : "destructive"
                                            }
                                            className="text-xs whitespace-nowrap"
                                        >
                                            {direction.minScore}+ баллов
                                        </Badge>
                                    </div>
                                </CardHeader>
                                <CardContent className="px-3 sm:px-4 pb-3">
                                    <CardDescription className="text-xs leading-tight mb-2">{direction.description}</CardDescription>

                                    <div className="flex items-center justify-between text-xs text-muted-foreground">
                                        <div className="flex items-center gap-3">
                                            <div className="flex items-center gap-1">
                                                <Clock className="w-3 h-3" />
                                                {direction.duration} года
                                            </div>
                                            <div className="flex items-center gap-1">
                                                <Users className="w-3 h-3" />
                                                {direction.places} мест
                                            </div>
                                        </div>
                                        {direction.isPopular && (
                                            <div className="flex items-center gap-1 text-yellow-600">
                                                <TrendingUp className="w-3 h-3" />
                                                <span>Популярное</span>
                                            </div>
                                        )}
                                    </div>

                                    <div className="mt-2 flex flex-wrap gap-1">
                                        {direction.subjects.slice(0, 2).map((subject, index) => (
                                            <Badge key={index} variant="outline" className="text-xs">
                                                {subject}
                                            </Badge>
                                        ))}
                                        {direction.subjects.length > 2 && (
                                            <Badge variant="outline" className="text-xs">
                                                +{direction.subjects.length - 2}
                                            </Badge>
                                        )}
                                    </div>
                                </CardContent>
                            </Card>
                        ))
                    )}
                </div>

                {/* Back Button */}
                <div className="mt-4 sm:mt-6">
                    <Button
                        variant="outline"
                        onClick={() => window.location.href = "/"}
                        className="w-full flex items-center justify-center gap-2 h-8 sm:h-9 text-xs sm:text-sm"
                    >
                        <ChevronLeft className="w-3 h-3" />
                        Вернуться к регистрации
                    </Button>
                </div>
            </div>
        </div>
    )
}
