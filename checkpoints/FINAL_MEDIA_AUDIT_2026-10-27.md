# Финальный аудит медиапубликации — 27.10.2026

**Проект:** «Петербург в деталях».  
**Область:** публичный медиакаталог и страница [«Для СМИ и партнёров»](https://spb-in-details.vercel.app/media/).  
**Результат:** **технические проверки пройдены; независимый браузерный визуальный/E2E-тест остаётся НЕ подтверждённым**.  
**Предыдущая контрольная точка:** [PROJECT_CHECKPOINT_2026-10-27.md](PROJECT_CHECKPOINT_2026-10-27.md).

## Проверенные факты

| Предмет | Результат | Подтверждение |
|---|---|---|
| Production deployment Vercel | PASS | Deployment `dpl_8JCfCDZMofhhGbGA8ybJ2CvK7kao`, `READY`, target `production`, alias `spb-in-details.vercel.app` |
| Исходный коммит production сайта | PASS | `9f67e72fec581cea8d39d7e1109845d3e09c56c6`, сайт из рабочего `DldaslsaA/SmartNavigator_SPb_Website_dev` |
| Генерация страницы `/media/` | PASS | Vercel build log: `/media/index.html` создан, `5 page(s) built`, `731` postbuild checks OK |
| Наличие ссылок на медиафайлы | PASS | Все 12 путей, сформированных функцией `file(...)` в `src/pages/media.astro`, присутствуют в `Media public/main` |
| Соответствие рабочих и публичных исходников | PASS | Git blob SHA файлов `media.astro`, `SiteHeader.astro`, `SiteFooter.astro` совпадают |
| Навигация | STATIC PASS | Desktop `SiteHeader` и мобильное меню используют общий `navItems`, ссылка `/media/` присутствует; footer также содержит ссылку |
| Адаптивность | STATIC PASS | CSS: `grid--two` использует `repeat(auto-fit, minmax(min(100%, 20rem), 1fr))`; на ширине ≤64 rem работает `nav-toggle`; это **анализ CSS, не визуальное измерение** |
| Приватность | STATIC PASS | Страница не содержит iframe, embedded video или сторонних video-скриптов; медиафайлы открываются по ссылкам на GitHub после действия пользователя |
| Проверенный медиапакет | PASS | 25 исходных медиафайлов; [Media CI](https://github.com/DenisAniskov/SPb_in_Details_Media_public/actions/runs/40552544596) ранее успешно проверил их SHA-256 |
| GitHub Releases | PASS | Android `v1.1.1`; Backend, Website, Media `source-2026.10.27` |
| Браузерный UI / HTTP smoke | **NOT TESTED** | Прямое HTTP-разрешение домена и просмотр страницы из проверочной среды оказались недоступны; скриншоты ПК/телефона не получены |

## Ссылки, проверенные в исходниках и дереве репозитория

```text
videos/horizontal/promo_1920x1080_v1.0.mp4
videos/horizontal/subtitles_ru.srt
videos/horizontal/poster.png
videos/vertical/promo_720x1280_v1.0.mp4
videos/vertical/subtitles_ru.srt
videos/vertical/cover.png
press/press_kit_v1.0.zip
presentation/app_presentation.pdf
print/marketing_brochure.pdf
documents/technical_passport.md
documents/marketing_passport.md
MEDIA_RIGHTS.md
```

Ссылка на папку `brand/` и прямая ссылка на Android Release проверялись отдельно по публичному GitHub, а не как `file(...)` ссылки.

## Что должен проверить человек в браузере

- [ ] Открыть <https://spb-in-details.vercel.app/media/> на ПК: заголовок, две видеокарточки, документы и блок прав отображаются без наложений
- [ ] Перейти на страницу из шапки сайта и из футера
- [ ] Открыть горизонтальный и вертикальный MP4, проверить их воспроизведение и звук
- [ ] Открыть пресс-кит ZIP, буклет PDF и презентацию PDF
- [ ] Открыть страницу на узком экране телефона: блоки идут в один столбец, мобильное меню раскрывается, горизонтального переполнения нет

## Решение и границы фиксации

**Исходники, ссылки, CI, успешная production-сборка и переключение домена в порядке.** Маркетинговая инфраструктура технически готова. До независимого визуального smoke-test корректный финальный статус: **`TECHNICALLY_VERIFIED / VISUAL_CHECK_PENDING`**. Не обозначать браузерный тест как выполненный без его фактического результата.

Этот отчёт фиксирует момент проверки; не изменяет теги `source-2026.10.27`, версии APK или рабочий сайт. Дальнейшее изменение `Media/main` только добавляет этот документ и ссылку на него.
