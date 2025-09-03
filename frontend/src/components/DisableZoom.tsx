"use client";

import { useEffect } from "react";

export function DisableZoom() {
    useEffect(() => {
        const metaViewport = document.querySelector('meta[name="viewport"]');
        if (!metaViewport) return;

        const disableZoom = () => {
            metaViewport.setAttribute(
                "content",
                "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"
            );
        };

        disableZoom();

        const observer = new MutationObserver(disableZoom);
        observer.observe(metaViewport, { attributes: true });

        return () => observer.disconnect();
    }, []);

    return null; // визуально ничего не рендерим
}
