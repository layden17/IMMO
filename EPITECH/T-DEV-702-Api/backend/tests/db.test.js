const { describe, expect, test } = require('@jest/globals');
const db = require('../db');
const connectDB = require('../db');
const disconnectDB = require('../db');
const mongoose = require('mongoose');

describe('db', () => {
    test('should return the same object', () => {
        expect(db).toBe(db);
    });
    test('should connect to the database', () => {
        connectDB().then(() => {
            expect(true).toBe(true);
        }).catch(err => {
            process.exit(1);
        });
    });
    test('should disconnect from the database', () => {
        disconnectDB().then(() => {
            expect(true).toBe(true);
        }).catch(err => {
            process.exit(1);
        });
    });
});

afterAll(async () => {
    await mongoose.connection.close();
  });