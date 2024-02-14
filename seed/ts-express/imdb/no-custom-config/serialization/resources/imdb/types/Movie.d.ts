/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedApi from "../../../../api";
import * as core from "../../../../core";
export declare const Movie: core.serialization.ObjectSchema<serializers.Movie.Raw, SeedApi.Movie>;
export declare namespace Movie {
    interface Raw {
        id: serializers.MovieId.Raw;
        title: string;
        rating: number;
    }
}