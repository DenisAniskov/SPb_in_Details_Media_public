# Контрольная точка проекта — 27 октября 2026 года

**Проект:** «Петербург в деталях» / SmartNavigator_SPb  
**Статус этапа:** публичные репозитории и медиапакет опубликованы; медиараздел включён в production deployment официального сайта.  
**Характер записи:** подтверждённый снимок состояния, а не новый релиз приложения и не изменение производства.  
**Дата проверки:** 27.10.2026 (МСК).

## 1. Публичные исходные снимки

| Компонент | Зафиксированный commit SHA | Публичный релиз |
|---|---|---|
| Android / Flutter | `6076d5bde3fdb34e0ba0ff049516016dc3621046` | [v1.1.1](https://github.com/DenisAniskov/SPb_in_Details_public/releases/tag/v1.1.1) |
| Backend / FastAPI | `0d870b59e837091f92f50b80ded9022c6f7463ee` | [source-2026.10.27](https://github.com/DenisAniskov/SPb_in_Details_Backend_public/releases/tag/source-2026.10.27) |
| Website public / Astro | `d3127c8debc7195f8250fc3d8347ed054048a760` | [source-2026.10.27](https://github.com/DenisAniskov/SPb_in_Details_Website_public/releases/tag/source-2026.10.27) |
| Media public | `73ee462ebfee1e927ad165d4dfee8ea5f740805d` | [source-2026.10.27](https://github.com/DenisAniskov/SPb_in_Details_Media_public/releases/tag/source-2026.10.27) |

SHA относятся к **опубликованным GitHub Releases**, а не к гарантированным исходникам действующего backend или к любым следующим коммитам `main`. Этот документ является последующим служебным коммитом Media и **не меняет** зафиксированный тег Media.

## 2. Сайт и развёртывание

- Официальный сайт: <https://spb-in-details.vercel.app/>.
- Новая страница для СМИ: <https://spb-in-details.vercel.app/media/>.
- Исходники этой страницы: [Website public, `src/pages/media.astro`](https://github.com/DenisAniskov/SPb_in_Details_Website_public/blob/d3127c8debc7195f8250fc3d8347ed054048a760/src/pages/media.astro).
- Рабочий репозиторий Vercel: `DldaslsaA/SmartNavigator_SPb_Website_dev`.
- Рабочий commit после [PR #8](https://github.com/DldaslsaA/SmartNavigator_SPb_Website_dev/pull/8): `9f67e72fec581cea8d39d7e1109845d3e09c56c6`.
- Vercel deployment: `dpl_8JCfCDZMofhhGbGA8ybJ2CvK7kao`.
- Проверка Vercel API: `READY`, target `production`, source ref `main`, SHA `9f67e72fec581cea8d39d7e1109845d3e09c56c6`; официальный alias `spb-in-details.vercel.app` привязан к этому deployment; `aliasError = null`.
- Публичный исходный сайт: [PR #3](https://github.com/DenisAniskov/SPb_in_Details_Website_public/pull/3) объединён. Редакции `src/pages/media.astro`, `SiteHeader.astro` и `SiteFooter.astro` в рабочих и публичных исходниках совпадали по Git blob SHA перед публикацией.

**Граница проверки:** состояние `READY` и привязка домена подтверждены через Vercel API. Независимое HTTP-открытие конечной страницы и визуальное тестирование в пользовательском браузере в этом сеансе **не выполнены** из-за ограничений сетевого доступа инструментов. Нельзя выдавать эти шаги за пройденный ручной E2E-тест. Простейшая финальная ручная проверка: открыть `/media/`, проверить меню, ссылки на оба MP4, на документы, на релиз Android и внешний вид на телефоне/ПК.

## 3. Медиапакет

- Состав: **25 медиафайлов**, включая горизонтальный Full HD MP4, вертикальный MP4, субтитры, исходники анимации, презентацию, буклет, пресс-кит и фирменные материалы.
- Публикация бинарных файлов: [Media PR #1](https://github.com/DenisAniskov/SPb_in_Details_Media_public/pull/1).
- Обновление статуса `RELEASED`: [Media PR #2](https://github.com/DenisAniskov/SPb_in_Details_Media_public/pull/2).
- Манифест: [`SOURCE_SHA256SUMS.txt`](../SOURCE_SHA256SUMS.txt), исходные контрольные суммы.
- [CI Media после публикации](https://github.com/DenisAniskov/SPb_in_Details_Media_public/actions/runs/40424144689): **SUCCESS**, проверка целостности файлов.
- [CI Website public](https://github.com/DenisAniskov/SPb_in_Details_Website_public/actions/runs/40424677394): **SUCCESS**, сборка Astro и проверки проекта.
- Публичные GitHub Releases Backend/Website/Media опубликованы без дополнительных `assets`: стандартные source ZIP и TAR.GZ предоставляет GitHub; исходный Media-репозиторий содержит также двоичные маркетинговые материалы.

## 4. Приложение и содержательные оговорки

- Публичный Android APK: **1.1.1+3**, Android 8.0 и новее. Источник загрузки — [официальный релиз v1.1.1](https://github.com/DenisAniskov/SPb_in_Details_public/releases/tag/v1.1.1).
- Редакционный каталог: **180 мест**, **35 исторических справок**.
- Smart Walk предлагает прогулку; пешеходная маршрутизация использует официальный Yandex MapKit.
- Shade, Quiet, Puddle и Pollen являются модельными оценками **не измерениями**, ИИ-ответы могут ошибаться, карта и маршруты требуют сеть.
- Видео — оригинальная **стилизованная графика**, а не актуальные снимки экрана Android. Архивные скриншоты старой версии приложения не должны представляться как v1.1.1.
- Права на бренд, медиа и сторонние данные не передаются автоматически через MIT-лицензию программного кода. См. [MEDIA_RIGHTS.md](../MEDIA_RIGHTS.md).
- Школьная работа, материалы защиты и связанные персональные реквизиты не входят в публичный медиапакет.

## 5. Границы фиксации и дальнейшие изменения

Это **информационный checkpoint**: он не блокирует новые коммиты, не создаёт новую Android-версию и не гарантирует неизменность живых сервисов. Для точной воспроизводимости используйте commit SHA и GitHub Releases выше. При следующем существенном выпуске создайте новый контрольный документ с новыми SHA; не переписывайте данный снимок.

**Заключение:** публичные GitHub релизы, пакет Media, исходники страницы `/media/`, успешный CI и соответствующий production deployment подтверждены. Ручной визуальный/HTTP smoke-test сайта остаётся рекомендованной внешней проверкой.
