import asyncio
import aiohttp
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from telegram.ext import ApplicationBuilder, CommandHandler
from urllib.parse import urlparse
import time
import os

TOKEN = '7648652939:AAH4Cz1LZnnDBxQEbiqwGUddm4M6qizFEMI'

PROXIES = [
    "http://PP_D4F1YGPKC1-country-UK:omf4xz27@evo-pro.porterproxies.com:61236",
    "http://PP_D4F1YGPKC1-country-SG:omf4xz27@evo-pro.porterproxies.com:61236",
    "http://PP_D4F1YGPKC1-country-TH:omf4xz27@evo-pro.porterproxies.com:61236",
    "http://PP_D4F1YGPKC1-country-PH:omf4xz27@evo-pro.porterproxies.com:61236",
    "http://PP_D4F1YGPKC1-country-MY:omf4xz27@evo-pro.porterproxies.com:61236",
    "http://PP_D4F1YGPKC1-country-MX:omf4xz27@evo-pro.porterproxies.com:61236",
    "http://PP_D4F1YGPKC1-country-JP:omf4xz27@evo-pro.porterproxies.com:61236",
    "http://PP_D4F1YGPKC1-country-EU:omf4xz27@evo-pro.porterproxies.com:61236",
]
ua = UserAgent()

def get_base_domain(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower().replace('www.', '')
        return domain
    except:
        return url

async def fetch(session, url, proxy=None):
    headers = {'User-Agent': ua.random}
    try:
        async with session.get(url, headers=headers, proxy=proxy, timeout=18) as response:
            return await response.text()
    except Exception:
        return None

async def duckduckgo_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}&s={page*50}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('.result__url') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

async def bing_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://www.bing.com/search?q={query.replace(' ', '+')}&first={page*10+1}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('li.b_algo h2 a') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

async def mojeek_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://www.mojeek.com/search?q={query.replace(' ', '+')}&s={page*10}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('ol.results li div.result > h2 > a') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

async def brave_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://search.brave.com/search?q={query.replace(' ', '+')}&page={page+1}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('a.result-header') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

async def qwant_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://www.qwant.com/?q={query.replace(' ', '+')}&t=web&p={page+1}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('a[data-testid=\"webResultLink\"]') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

async def yandex_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://yandex.com/search/?text={query.replace(' ', '+')}&p={page}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('a.Link') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

async def startpage_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://www.startpage.com/sp/search?q={query.replace(' ', '+')}&page={page+1}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('a.w-gl__result-title') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

async def metager_search(query, max_results=60):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://metager.org/meta/meta.ger3?eingabe={query.replace(' ', '+')}&page={page+1}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('.result .title a') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.5, 1.2))
    return list(results)

# --- Shopify/Shop Pay fingerprint detection ---
def is_shopify_site(url, html):
    if "myshopify.com" in url.lower():
        return True
    if not html:
        return False
    h = html.lower()
    if ('cdn.shopify.com' in h or 'x-shopify' in h or 'shopify' in h or
        'assets/shopify' in h or 'shopify-section' in h or
        'powered by shopify' in h or 'meta name="generator" content="shopify"' in h):
        return True
    return False

def has_shop_pay(html):
    if not html:
        return False
    h = html.lower()
    return ("shop pay" in h or "shoppay" in h)

async def filter_by_shopify_and_shoppay(urls, keywords):
    matched = []
    sem = asyncio.Semaphore(20)
    keywords = [k.lower() for k in keywords]
    seen_domains = set()

    async def check_url(url):
        domain = get_base_domain(url)
        if domain in seen_domains:
            return
        async with sem:
            async with aiohttp.ClientSession(headers={'User-Agent': ua.random}) as session:
                html = await fetch(session, url, proxy=random.choice(PROXIES))
                if not html: return
                if not is_shopify_site(url, html): return
                if not has_shop_pay(html): return
                if not all(k in html.lower() for k in keywords): return
                seen_domains.add(domain)
                matched.append(url.strip())
    await asyncio.gather(*(check_url(url) for url in urls))
    return matched

async def start(update, context):
    await update.message.reply_text(
        "🤖 /dork <keyword(s)> — finds all Shopify stores (even private/custom domain) with Shop Pay. Example: /dork t-shirt"
    )

async def handle_dork(update, context):
    if context.args:
        keywords = context.args
        query = ' '.join(keywords)
        msg = await update.message.reply_text(f"🔍 Searching all free engines for Shopify + Shop Pay stores: {query}")

        # Advanced Shopify dorking
        dorks = [
            f'inurl:myshopify {query}',
            f'inurl:collections {query}',
            f'inurl:cart {query}',
            f'inurl:products {query}',
            f'"powered by shopify" {query}',
            f'"shopify" {query}',
        ]

        # Launch all tasks concurrently
        search_tasks = []
        for dork in dorks:
            search_tasks += [
                duckduckgo_search(dork, 20),
                bing_search(dork, 20),
                mojeek_search(dork, 20),
                brave_search(dork, 20),
                qwant_search(dork, 20),
                yandex_search(dork, 20),
                startpage_search(dork, 20),
                metager_search(dork, 20)
            ]
        all_results = await asyncio.gather(*search_tasks)
        all_urls = set()
        for res in all_results:
            all_urls.update(res)
        all_urls = list(all_urls)

        await msg.edit_text(f"🌐 Found {len(all_urls)} candidate URLs, checking for Shopify + Shop Pay & deduping...")

        filtered_urls = await filter_by_shopify_and_shoppay(all_urls, keywords)

        filename = f'shopify_shoppay_{int(time.time())}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            for url in filtered_urls:
                f.write(url + '\n')
        with open(filename, 'rb') as f:
            await update.message.reply_document(document=f, filename=filename)
        os.remove(filename)

        await msg.edit_text(f"✅ Done! {len(filtered_urls)} unique Shopify + Shop Pay sites found (all free APIs).")
    else:
        await update.message.reply_text("❗ Use the command like: /dork t-shirt")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('dork', handle_dork))
    print('🛒 Private/Public Shopify+ShopPay Finder (All Free APIs) running...')
    app.run_polling()
