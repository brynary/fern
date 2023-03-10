import { Values } from "@fern-api/core-utils";
import {
    ErrorDeclarationSchema,
    ExampleEndpointCallSchema,
    ExampleResponseSchema,
    ExampleTypeReferenceSchema,
    ExampleTypeSchema,
    HttpEndpointSchema,
    HttpHeaderSchema,
    HttpPathParameterSchema,
    HttpQueryParameterSchema,
    HttpServiceSchema,
    TypeDeclarationSchema,
} from "../schemas";
import { NodePath } from "./NodePath";

export type FernDefinitionFileAstVisitor<R = void | Promise<void>> = {
    [K in keyof FernDefinitionFileAstNodeTypes]: FernDefinitionFileAstNodeVisitor<K, R>;
};

export interface FernDefinitionFileAstNodeTypes {
    docs: string;
    import: { importPath: string; importedAs: string };
    typeDeclaration: {
        typeName: TypeDeclarationName;
        declaration: TypeDeclarationSchema;
    };
    exampleType: { typeName: string; typeDeclaration: TypeDeclarationSchema; example: ExampleTypeSchema };
    exampleTypeReference: string;
    typeReference: { typeReference: string; location?: TypeReferenceLocation };
    typeName: string;
    httpService: HttpServiceSchema;
    httpEndpoint: { endpointId: string; endpoint: HttpEndpointSchema; service: HttpServiceSchema };
    streamCondition: { streamCondition: string | undefined; endpoint: HttpEndpointSchema };
    exampleHttpEndpointCall: {
        example: ExampleEndpointCallSchema;
        endpoint: HttpEndpointSchema;
        service: HttpServiceSchema;
    };
    exampleHeaders: {
        examples: Record<string, ExampleTypeReferenceSchema> | undefined;
        endpoint: HttpEndpointSchema;
        service: HttpServiceSchema;
    };
    examplePathParameters: {
        examples: Record<string, ExampleTypeReferenceSchema> | undefined;
        endpoint: HttpEndpointSchema;
        service: HttpServiceSchema;
    };
    exampleQueryParameters: {
        examples: Record<string, ExampleTypeReferenceSchema> | undefined;
        endpoint: HttpEndpointSchema;
        service: HttpServiceSchema;
    };
    exampleRequest: {
        example: ExampleTypeReferenceSchema | undefined;
        endpoint: HttpEndpointSchema;
        service: HttpServiceSchema;
    };
    exampleResponse: {
        example: ExampleResponseSchema | undefined;
        endpoint: HttpEndpointSchema;
        service: HttpServiceSchema;
    };
    pathParameter: { pathParameterKey: string; pathParameter: HttpPathParameterSchema };
    queryParameter: { queryParameterKey: string; queryParameter: HttpQueryParameterSchema };
    header: { headerKey: string; header: HttpHeaderSchema };
    errorDeclaration: { errorName: string; declaration: ErrorDeclarationSchema };
    errorReference: string;
}

export type TypeDeclarationName = { isInlined: false; name: string } | { isInlined: true; location: "inlinedRequest" };

export const TypeReferenceLocation = {
    InlinedRequestProperty: "inlinedRequestProperty",
} as const;
export type TypeReferenceLocation = Values<typeof TypeReferenceLocation>;

export type FernDefinitionFileAstNodeVisitor<
    K extends keyof FernDefinitionFileAstNodeTypes,
    R = void | Promise<void>
> = (node: FernDefinitionFileAstNodeTypes[K], nodePath: NodePath) => R;