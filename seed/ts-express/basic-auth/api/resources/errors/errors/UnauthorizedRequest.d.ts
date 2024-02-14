/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as errors from "../../../../errors";
import * as SeedBasicAuth from "../../..";
import express from "express";
export declare class UnauthorizedRequest extends errors.SeedBasicAuthError {
    private readonly body;
    constructor(body: SeedBasicAuth.UnauthorizedRequestErrorBody);
    send(res: express.Response): Promise<void>;
}