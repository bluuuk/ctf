import puppeteer from "puppeteer";

const browser = await puppeteer.launch({
  args: ["--no-sandbox"],
});
browser.setCookie({
  domain: process.env.DOMAIN,
  httpOnly: false,
  expires: -1,
  name: "flag",
  value: process.env.FLAG,
  path: "/",
});

const page = await browser.newPage();

await page.goto(`http://${process.env.DOMAIN}`);

while (true) {
  console.log("Refreshing Website");
  await page.reload();

  // Reload once per minute
  await sleep(60000);
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
