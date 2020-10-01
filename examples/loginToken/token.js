const puppeteer = require("puppeteer");
const fs = require("fs");

const email = "<email>";
const password = "<password>";

const getToken = async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto("https://app.senecalearning.com/login");
  await page.waitForSelector(
    ".SignUpFormDumbWrapper_wrapper__rzuxI > .SignUpFormDumbWrapper_outerWrapper__3SmUr > .common_form__19F57"
  );
  await page.type(
    ".SignUpFormDumbWrapper_wrapper__rzuxI > .SignUpFormDumbWrapper_outerWrapper__3SmUr > .common_form__19F57 > .FieldLabelWrapper > .SettingsFormInput__input",
    email
  );
  await page.type(
    ".SignUpFormDumbWrapper_wrapper__rzuxI > .SignUpFormDumbWrapper_outerWrapper__3SmUr > .common_form__19F57 > .common_inputWrapper__3gShC > .FieldLabelWrapper > .SettingsFormInput__input",
    password
  );
  await page.waitForSelector(
    ".common_form__19F57 > .Button_button__1Q4K4 > .Button_content__1Q0Uw > .Button_iconTextWrapper__2AVyk > span"
  );
  await page.click(
    ".common_form__19F57 > .Button_button__1Q4K4 > .Button_content__1Q0Uw > .Button_iconTextWrapper__2AVyk > span"
  );
  page.on("response", async (response) => {
    if (
      response.url() == "https://identity.app.senecalearning.com/" &&
      response.headers()["content-length"] > 3000
    ) {
      filewrite = fs.writeFile(
        `${__dirname}/token.txt`,
        (await response.json())["AuthenticationResult"]["RefreshToken"],
        async (err) => {
          if (err) {
            console.log(err);
            return false;
          }
          console.log("The file was saved!");
          await browser.close();
          return true;
        }
      );
      if (filewrite === true) {
        return;
      }
    }
  });
};

getToken();
