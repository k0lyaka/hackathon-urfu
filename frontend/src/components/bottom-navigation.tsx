"use client"

import { Home, Info } from "lucide-react"
import Link from "next/link"
import { usePathname } from "next/navigation"

export default function BottomNavigation() {
    const pathname = usePathname()

    const navItems = [
        {
            href: "/",
            icon: Home,
            label: "Главная",
            active: pathname === "/" || pathname === "/directions",
        },
        {
            href: "/about",
            icon: Info,
            label: "О нас",
            active: pathname === "/about",
        },
    ]

    return (
        <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-50">
            <div className="flex justify-around items-center h-16 px-2">
                {navItems.map((item) => {
                    const Icon = item.icon
                    return (
                        <Link
                            key={item.href}
                            href={item.href}
                            className={`flex flex-col items-center justify-center flex-1 py-2 px-1 transition-colors ${
                                item.active ? "text-red-600" : "text-gray-500 hover:text-red-500"
                            }`}
                        >
                            <Icon className="w-5 h-5 mb-1" />
                            <span className="text-xs font-medium">{item.label}</span>
                        </Link>
                    )
                })}
            </div>
        </nav>
    )
}
