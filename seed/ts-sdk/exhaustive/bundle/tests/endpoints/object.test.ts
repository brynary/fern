/**
 * This file was auto-generated by Fern from our API Definition.
 */

import { FiddleClient } from "../../src/Client";

const client = new FiddleClient({
    environment: process.env.TESTS_BASE_URL || "test",
    token: process.env.TESTS_AUTH || "test",
});

describe("Object_", () => {
    test("getAndReturnWithOptionalField", async () => {
        const response = await client.endpoints.object.getAndReturnWithOptionalField({
            string: "string",
            integer: 1,
            long: 1000000,
            double: 1.1,
            bool: true,
            datetime: new Date("2024-01-15T09:30:00.000Z"),
            date: "2023-01-15",
            uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            base64: "SGVsbG8gd29ybGQh",
            list: ["string"],
            set: new Set(["string"]),
            map: {
                1: "string",
            },
        });
        expect(response).toEqual({
            string: "string",
            integer: 1,
            long: 1000000,
            double: 1.1,
            bool: true,
            datetime: new Date("2024-01-15T09:30:00.000Z"),
            date: "2023-01-15",
            uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            base64: "SGVsbG8gd29ybGQh",
            list: ["string"],
            set: ["string"],
            map: { "1": "string" },
        });
    });

    test("getAndReturnWithRequiredField", async () => {
        const response = await client.endpoints.object.getAndReturnWithRequiredField({
            string: "string",
        });
        expect(response).toEqual({ string: "string" });
    });

    test("getAndReturnWithMapOfMap", async () => {
        const response = await client.endpoints.object.getAndReturnWithMapOfMap({
            map: {
                string: {
                    string: "string",
                },
            },
        });
        expect(response).toEqual({ map: { string: { string: "string" } } });
    });

    test("getAndReturnNestedWithOptionalField", async () => {
        const response = await client.endpoints.object.getAndReturnNestedWithOptionalField({
            string: "string",
            nestedObject: {
                string: "string",
                integer: 1,
                long: 1000000,
                double: 1.1,
                bool: true,
                datetime: new Date("2024-01-15T09:30:00.000Z"),
                date: "2023-01-15",
                uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                base64: "SGVsbG8gd29ybGQh",
                list: ["string"],
                set: new Set(["string"]),
                map: {
                    1: "string",
                },
            },
        });
        expect(response).toEqual({
            string: "string",
            nestedObject: {
                string: "string",
                integer: 1,
                long: 1000000,
                double: 1.1,
                bool: true,
                datetime: new Date("2024-01-15T09:30:00.000Z"),
                date: "2023-01-15",
                uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                base64: "SGVsbG8gd29ybGQh",
                list: ["string"],
                set: ["string"],
                map: { "1": "string" },
            },
        });
    });

    test("getAndReturnNestedWithRequiredField", async () => {
        const response = await client.endpoints.object.getAndReturnNestedWithRequiredField({
            string: "string",
            nestedObject: {
                string: "string",
                integer: 1,
                long: 1000000,
                double: 1.1,
                bool: true,
                datetime: new Date("2024-01-15T09:30:00.000Z"),
                date: "2023-01-15",
                uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                base64: "SGVsbG8gd29ybGQh",
                list: ["string"],
                set: new Set(["string"]),
                map: {
                    1: "string",
                },
            },
        });
        expect(response).toEqual({
            string: "string",
            nestedObject: {
                string: "string",
                integer: 1,
                long: 1000000,
                double: 1.1,
                bool: true,
                datetime: new Date("2024-01-15T09:30:00.000Z"),
                date: "2023-01-15",
                uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                base64: "SGVsbG8gd29ybGQh",
                list: ["string"],
                set: ["string"],
                map: { "1": "string" },
            },
        });
    });

    test("getAndReturnNestedWithRequiredFieldAsList", async () => {
        const response = await client.endpoints.object.getAndReturnNestedWithRequiredFieldAsList([
            {
                string: "string",
                nestedObject: {
                    string: "string",
                    integer: 1,
                    long: 1000000,
                    double: 1.1,
                    bool: true,
                    datetime: new Date("2024-01-15T09:30:00.000Z"),
                    date: "2023-01-15",
                    uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    base64: "SGVsbG8gd29ybGQh",
                    list: ["string"],
                    set: new Set(["string"]),
                    map: {
                        1: "string",
                    },
                },
            },
        ]);
        expect(response).toEqual({
            string: "string",
            nestedObject: {
                string: "string",
                integer: 1,
                long: 1000000,
                double: 1.1,
                bool: true,
                datetime: new Date("2024-01-15T09:30:00.000Z"),
                date: "2023-01-15",
                uuid: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                base64: "SGVsbG8gd29ybGQh",
                list: ["string"],
                set: ["string"],
                map: { "1": "string" },
            },
        });
    });
});