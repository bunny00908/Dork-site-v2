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
        async with session.get(url, headers=headers, proxy=proxy, timeout=7) as response:
            return await response.text()
    except Exception:
        return None

async def duckduckgo_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def bing_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def mojeek_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def brave_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def qwant_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def yandex_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def startpage_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def metager_search(query, max_results=10):
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
            await asyncio.sleep(random.uniform(0.4, 1.1))
    return list(results)

async def gigablast_search(query, max_results=10):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://www.gigablast.com/search?q={query.replace(' ', '+')}&n=30&s={page*30}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('div.res h3 a') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.6, 1.2))
    return list(results)

async def exalead_search(query, max_results=10):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://www.exalead.com/search/web/results/?q={query.replace(' ', '+')}&start={page*10}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('.result_title a') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.6, 1.2))
    return list(results)

async def seznam_search(query, max_results=10):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://search.seznam.cz/?q={query.replace(' ', '+')}&from={page*10}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('.result h3 a') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.6, 1.2))
    return list(results)

async def yep_search(query, max_results=10):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://yep.com/web?q={query.replace(' ', '+')}&start={page*10}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('a.result-link') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.6, 1.2))
    return list(results)

async def swisscows_search(query, max_results=10):
    results, page = set(), 0
    async with aiohttp.ClientSession() as session:
        while len(results) < max_results:
            search_url = f"https://swisscows.com/web?query={query.replace(' ', '+')}&page={page+1}"
            proxy = random.choice(PROXIES)
            html = await fetch(session, search_url, proxy)
            if not html: break
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.select('a.swisscows-result__link') if a.get('href')]
            if not links: break
            results.update(links)
            page += 1
            await asyncio.sleep(random.uniform(0.6, 1.2))
    return list(results)

async def start(update, context):
    await update.message.reply_text(
        "🤖 /dork <keyword(s)> — finds all links (deduped, no filtering, all APIs). Example: /dork t-shirt"
    )

async def handle_dork(update, context):
    if context.args:
        keywords = context.args
        query = ' '.join(keywords)
        msg = await update.message.reply_text(f"🔍 Scraping all free engines for all links: {query}")

        dorks = [
            f'inurl:myshopify {query}',
            f'inurl:collections {query}',
            f'inurl:cart {query}',
            f'inurl:products {query}',
            f'"powered by shopify" {query}',
            f'"shopify" {query}',
        ]

        search_tasks = []
        for dork in dorks:
            search_tasks += [
                duckduckgo_search(dork, 10),
                bing_search(dork, 10),
                mojeek_search(dork, 10),
                brave_search(dork, 10),
                qwant_search(dork, 10),
                yandex_search(dork, 10),
                startpage_search(dork, 10),
                metager_search(dork, 10),
                gigablast_search(dork, 10),
                exalead_search(dork, 10),
                seznam_search(dork, 10),
                yep_search(dork, 10),
                swisscows_search(dork, 10)
            ]
        all_results = await asyncio.gather(*search_tasks)
        all_urls = []
        for res in all_results:
            all_urls += res

        # Deduplicate by domain
        unique_domains = set()
        unique_urls = []
        for url in all_urls:
            base = get_base_domain(url)
            if base not in unique_domains:
                unique_domains.add(base)
                unique_urls.append(url.strip())

        filename = f'dork_links_{int(time.time())}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            for url in unique_urls:
                f.write(url + '\n')
        with open(filename, 'rb') as f:
            await update.message.reply_document(document=f, filename=filename)
        os.remove(filename)

        await msg.edit_text(f"✅ Done! {len(unique_urls)} unique links found (ALL free APIs, max speed).")
    else:
        await update.message.reply_text("❗ Use the command like: /dork t-shirt")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('dork', handle_dork))
    print('⚡️ Dork Bot (all APIs, no filtering, max speed) running...')
    app.run_polling()
