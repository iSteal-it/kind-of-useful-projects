var url = null;
url = process.argv[2];
if (!url) leave("URL must be provided");

const puppeteer = require('puppeteer-core');
let browser, ad_links;
(async() => {
    try {
        console.log("Bot started");
        let count = 1;
        while (true) {
            console.log(`Processing ${count}...`);
            browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: process.argv[3] === "-s" ? false : true });
            var page = await browser.newPage();
            await page.goto(url, { timeout: 0 });

            await page.waitForTimeout(10000);
            ad_links = [];
            await getAdLinks(page);
            console.log(`  Found ${ad_links.length} ads`);
            for (let i = 0; i < ad_links.length; i++) {
                await page.waitForTimeout(Math.random() * 3000);
                await ad_links[i].page.evaluate(el => el.click(), ad_links[i].link);
                console.log(`  Clicked ad ${i + 1}`);
                try {
                    const new_page_promise = new Promise(x => browser.once('targetcreated', target => x(target.page())));
                    await Promise.race([new_page_promise, wait(5000)]);
                } catch (e) {}
                const pages = await browser.pages();
                if (pages.length === 3) {
                    page = pages[pages.length - 1];
                    await page.bringToFront();
                    await page.waitForTimeout(3000);
                    console.log("    Page opened");
                    await page.waitForTimeout(Math.random() * 3000);
                    await scrollDown(page); //Scroll down
                    console.log("    Scrolled");
                    await page.waitForTimeout(Math.random() * 3000);
                    await page.close();
                    page = pages[pages.length - 2];
                }
            }
            await browser.close();
            console.log(`Done ${count++}! Starting again after 15 seconds...\n`);
            await wait(15000); //Wait for 15 seconds
        }
    } catch (e) {
        browser.close();
        leave("There has been an error! Please try again");
        return;
    }
})();

function leave(message) {
    console.error(message);
    process.exit(1);
}
async function scrollDown(page) {
    try {
        var current = 0,
            total;
        do {
            let dy = Math.random() * 4000 + 50;
            total = await page.evaluate(dy => {
                window.scrollBy(0, dy);
                return document.body.scrollHeight;
            }, dy);
            current += dy;
            await page.waitForTimeout(Math.random() * 2000 + 500);
        } while (current <= total)
    } catch (e) {}
}

function wait(ms) {
    return new Promise(resolve => {
        setTimeout(() => { resolve() }, ms);
    });
}
async function getAdLinks(page) {
    const links = await page.$$('a');
    for (let link of links) {
        const href = await page.evaluate(el => el.getAttribute("href"), link);
        if (/(googleadservices|googleads|zemanta|adclick)/.test(href)) ad_links.push({ page: page, link: link });
    }
    const iframes = await page.$$('iframe');
    for (let frame of iframes) {
        await Promise.race([getAdLinks(await frame.contentFrame()), wait(5000)]);
    }
}
