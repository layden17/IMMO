/** @type {import('jest').Config} */
const config = {
  preset: "@shelf/jest-mongodb",
  setupFiles: ["<rootDir>/tests/jest.setup.js"],
};
module.exports = config;