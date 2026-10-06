from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Dict, Any


BRAND = {
    "company": "FoxSD",
    "alias": "Fox",
    "email": "foxsd520@gmail.com",
}


@dataclass
class PromptIntent:
    topic: str
    confidence: float
    tags: List[str]


class FoxSDReasoner:
    """Lightweight local reasoning layer for FoxSD AI."""

    def __init__(self):
        self.brand = BRAND

    def detect_intent(self, text: str) -> PromptIntent:
        lowered = text.lower()
        tags = []

        if any(word in lowered for word in ["برمجة", "code", "programming", "function", "api", "python", "javascript", "node", "react", "backend", "frontend"]):
            tags.append("programming")
        if any(word in lowered for word in ["امن", "security", "cyber", "penetration", "vulnerability", "sql injection", "xss", "csrf", "owasp", "auth"]):
            tags.append("cybersecurity")
        if any(word in lowered for word in ["موقع", "website", "site", "landing page", "frontend", "ui", "ux", "css", "html", "wordpress", "nextjs"]):
            tags.append("web-development")
        if any(word in lowered for word in ["تطبيق", "app", "mobile", "android", "ios", "desktop", "flutter", "react native"]):
            tags.append("app-development")
        if any(word in lowered for word in ["business", "project", "plan", "strategy", "startup", "analysis"]):
            tags.append("business")

        if not tags:
            tags = ["general"]

        topic = max(tags, key=lambda tag: 1 if tag == "general" else 0)
        confidence = 0.82 if len(tags) == 1 else 0.9

        return PromptIntent(topic=topic, confidence=confidence, tags=tags)

    def build_answer(self, text: str) -> Dict[str, Any]:
        intent = self.detect_intent(text)

        suggestions = {
            "programming": [
                "حدث اللغة المطلوبة: Python, JavaScript, TypeScript, Go, Rust, Java, C#, PHP, Java, Ruby.",
                "حدث نوع المشروع: API, CLI, backend, frontend, full-stack, desktop, data pipeline.",
                "أعطني بنية المشروع وواجهات الإدخال والإخراج.",
            ],
            "cybersecurity": [
                "حدث الهدف: اختبار اختراق، تحليل الثغرات، مراجعة أمنية، حماية التطبيق، أمن البنية.",
                "وضح نوع النظام: web, mobile, cloud, API, infrastructure.",
                "إذا رغبت، أستطيع كتابة تقييم OWASP، خطة اختبار، أو سيناريوهات التخفيف.",
            ],
            "web-development": [
                "حدث نوع الموقع: متجر، منصة، موقع شخصي، خدمات، شركة، SaaS.",
                "حدث اللغة/الإطار: HTML, CSS, JS, React, Next.js, Node.js, PHP, Laravel.",
                "أذكر هل يريد تصميم احترافي، لوحة تحكم، تسجيل دخول، دفع، API، أو CRM.",
            ],
            "app-development": [
                "حدث نوع التطبيق: Android, iOS, desktop, PWA, dashboard, ERP, business app.",
                "حدث إطار التطوير: Flutter, React Native, Ionic, .NET MAUI, Electron.",
                "أخبرني إن كان التطبيق يحتاج إلى Auth, DB, real-time sync, payments, notifications.",
            ],
            "business": [
                "حدث الهدف التجاري: زيادة المبيعات، تحسين الخدمة، بناء نظام داخلي، أتمتة العمليات.",
                "اذكر حجم المشروع، الفئة المستهدفة، أدوات التشغيل الحالية.",
                "أستطيع بناء خطة تنفيذ، مخطط أولي، أو استراتيجية التشغيل.",
            ],
            "general": [
                "أخبرني أكثر حول المطلوب حتى أستطيع تقديم إجابة دقيقة ومفيدة.",
                "إذا كان الطلب تقنيًا، أذكر التقنية والهدف واللغة المطلوبة.",
            ],
        }

        return {
            "brand": BRAND,
            "intent": intent,
            "answer": "أنا FoxSD AI، أعمل كـ مساعد تقني وتجاري متخصص. أستطيع مساعدتك في البرمجة، الأمن السيبراني، تصميم المواقع والتطبيقات، وتحويل الفكرة إلى نظام عملي.\n\n" + "\n".join(suggestions.get(intent.topic, suggestions["general"])),
            "timestamp": datetime.utcnow().isoformat(),
        }


if __name__ == "__main__":
    ai = FoxSDReasoner()
    sample = "أريد بناء نظام موقع كامل مع تسجيل دخول وأمان وحفظ بيانات"
    result = ai.build_answer(sample)
    print(json.dumps(result, ensure_ascii=False, indent=2))
