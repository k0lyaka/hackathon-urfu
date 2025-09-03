"use client"

import { ArrowLeft, Users, Target, Award, Mail, Phone, MapPin } from "lucide-react"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"

export default function AboutPage() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-red-50 pb-20">
            <div className="container mx-auto px-4 py-6 max-w-2xl">
                {/* Header */}
                <div className="flex items-center gap-4 mb-6">
                    <Link href="/">
                        <Button variant="ghost" size="sm" className="p-2">
                            <ArrowLeft className="w-4 h-4" />
                        </Button>
                    </Link>
                    <h1 className="text-2xl font-bold text-gray-900">О нас</h1>
                </div>

                {/* University Info */}
                <Card className="mb-6 border-red-100">
                    <CardContent className="p-6">
                        <div className="text-center mb-6">
                            <div className="w-16 h-16 bg-red-600 rounded-full flex items-center justify-center mx-auto mb-4">
                                <span className="text-white font-bold text-xl">УрФУ</span>
                            </div>
                            <h2 className="text-xl font-bold text-gray-900 mb-2">Уральский федеральный университет</h2>
                            <p className="text-gray-600 text-sm">имени первого Президента России Б.Н. Ельцина</p>
                        </div>
                    </CardContent>
                </Card>

                {/* Mission & Values */}
                <div className="space-y-4 mb-6">
                    <Card className="border-blue-100">
                        <CardContent className="p-4">
                            <div className="flex items-start gap-3">
                                <div className="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <Target className="w-4 h-4 text-blue-600" />
                                </div>
                                <div>
                                    <h3 className="font-semibold text-gray-900 mb-2">Наша миссия</h3>
                                    <p className="text-sm text-gray-600">
                                        Подготовка высококвалифицированных специалистов и развитие научных исследований для инновационного
                                        развития России и мира.
                                    </p>
                                </div>
                            </div>
                        </CardContent>
                    </Card>

                    <Card className="border-red-100">
                        <CardContent className="p-4">
                            <div className="flex items-start gap-3">
                                <div className="w-8 h-8 bg-red-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <Users className="w-4 h-4 text-red-600" />
                                </div>
                                <div>
                                    <h3 className="font-semibold text-gray-900 mb-2">Студенческое сообщество</h3>
                                    <p className="text-sm text-gray-600">
                                        Более 35 000 студентов из 80+ стран мира обучаются в УрФУ по различным направлениям подготовки.
                                    </p>
                                </div>
                            </div>
                        </CardContent>
                    </Card>

                    <Card className="border-blue-100">
                        <CardContent className="p-4">
                            <div className="flex items-start gap-3">
                                <div className="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <Award className="w-4 h-4 text-blue-600" />
                                </div>
                                <div>
                                    <h3 className="font-semibold text-gray-900 mb-2">Достижения</h3>
                                    <p className="text-sm text-gray-600">
                                        УрФУ входит в топ-10 российских университетов и является участником программы "5-100" по повышению
                                        конкурентоспособности.
                                    </p>
                                </div>
                            </div>
                        </CardContent>
                    </Card>
                </div>

                {/* Contact Info */}
                <Card className="border-gray-200">
                    <CardContent className="p-4">
                        <h3 className="font-semibold text-gray-900 mb-4">Контактная информация</h3>
                        <div className="space-y-3">
                            <div className="flex items-center gap-3">
                                <MapPin className="w-4 h-4 text-gray-500" />
                                <span className="text-sm text-gray-600">г. Екатеринбург, ул. Мира, 19</span>
                            </div>
                            <div className="flex items-center gap-3">
                                <Phone className="w-4 h-4 text-gray-500" />
                                <span className="text-sm text-gray-600">+7 (343) 375-44-44</span>
                            </div>
                            <div className="flex items-center gap-3">
                                <Mail className="w-4 h-4 text-gray-500" />
                                <span className="text-sm text-gray-600">info@urfu.ru</span>
                            </div>
                        </div>
                    </CardContent>
                </Card>
            </div>
        </div>
    )
}
