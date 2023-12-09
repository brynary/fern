/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.exhaustive.resources.endpoints.object;

import com.seed.exhaustive.core.ApiError;
import com.seed.exhaustive.core.ClientOptions;
import com.seed.exhaustive.core.MediaTypes;
import com.seed.exhaustive.core.ObjectMappers;
import com.seed.exhaustive.core.RequestOptions;
import com.seed.exhaustive.resources.types.object.types.NestedObjectWithOptionalField;
import com.seed.exhaustive.resources.types.object.types.NestedObjectWithRequiredField;
import com.seed.exhaustive.resources.types.object.types.ObjectWithMapOfMap;
import com.seed.exhaustive.resources.types.object.types.ObjectWithOptionalField;
import com.seed.exhaustive.resources.types.object.types.ObjectWithRequiredField;
import java.io.IOException;
import okhttp3.Headers;
import okhttp3.HttpUrl;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class ObjectClient {
    protected final ClientOptions clientOptions;

    public ObjectClient(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
    }

    public ObjectWithOptionalField getAndReturnWithOptionalField() {
        return getAndReturnWithOptionalField(ObjectWithOptionalField.builder().build());
    }

    public ObjectWithOptionalField getAndReturnWithOptionalField(
            ObjectWithOptionalField request, RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .addPathSegments("object")
                .addPathSegments("get-and-return-with-optional-field")
                .build();
        RequestBody body;
        try {
            body = RequestBody.create(
                    ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        Request okhttpRequest = new Request.Builder()
                .url(httpUrl)
                .method("POST", body)
                .headers(Headers.of(clientOptions.headers(requestOptions)))
                .addHeader("Content-Type", "application/json")
                .build();
        try {
            Response response =
                    clientOptions.httpClient().newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), ObjectWithOptionalField.class);
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public ObjectWithOptionalField getAndReturnWithOptionalField(ObjectWithOptionalField request) {
        return getAndReturnWithOptionalField(request, null);
    }

    public ObjectWithRequiredField getAndReturnWithRequiredField(
            ObjectWithRequiredField request, RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .addPathSegments("object")
                .addPathSegments("get-and-return-with-required-field")
                .build();
        RequestBody body;
        try {
            body = RequestBody.create(
                    ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        Request okhttpRequest = new Request.Builder()
                .url(httpUrl)
                .method("POST", body)
                .headers(Headers.of(clientOptions.headers(requestOptions)))
                .addHeader("Content-Type", "application/json")
                .build();
        try {
            Response response =
                    clientOptions.httpClient().newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), ObjectWithRequiredField.class);
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public ObjectWithRequiredField getAndReturnWithRequiredField(ObjectWithRequiredField request) {
        return getAndReturnWithRequiredField(request, null);
    }

    public ObjectWithMapOfMap getAndReturnWithMapOfMap(ObjectWithMapOfMap request, RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .addPathSegments("object")
                .addPathSegments("get-and-return-with-map-of-map")
                .build();
        RequestBody body;
        try {
            body = RequestBody.create(
                    ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        Request okhttpRequest = new Request.Builder()
                .url(httpUrl)
                .method("POST", body)
                .headers(Headers.of(clientOptions.headers(requestOptions)))
                .addHeader("Content-Type", "application/json")
                .build();
        try {
            Response response =
                    clientOptions.httpClient().newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), ObjectWithMapOfMap.class);
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public ObjectWithMapOfMap getAndReturnWithMapOfMap(ObjectWithMapOfMap request) {
        return getAndReturnWithMapOfMap(request, null);
    }

    public NestedObjectWithOptionalField getAndReturnNestedWithOptionalField() {
        return getAndReturnNestedWithOptionalField(
                NestedObjectWithOptionalField.builder().build());
    }

    public NestedObjectWithOptionalField getAndReturnNestedWithOptionalField(
            NestedObjectWithOptionalField request, RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .addPathSegments("object")
                .addPathSegments("get-and-return-nested-with-optional-field")
                .build();
        RequestBody body;
        try {
            body = RequestBody.create(
                    ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        Request okhttpRequest = new Request.Builder()
                .url(httpUrl)
                .method("POST", body)
                .headers(Headers.of(clientOptions.headers(requestOptions)))
                .addHeader("Content-Type", "application/json")
                .build();
        try {
            Response response =
                    clientOptions.httpClient().newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return ObjectMappers.JSON_MAPPER.readValue(
                        response.body().string(), NestedObjectWithOptionalField.class);
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public NestedObjectWithOptionalField getAndReturnNestedWithOptionalField(NestedObjectWithOptionalField request) {
        return getAndReturnNestedWithOptionalField(request, null);
    }

    public NestedObjectWithRequiredField getAndReturnNestedWithRequiredField(
            NestedObjectWithRequiredField request, RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .addPathSegments("object")
                .addPathSegments("get-and-return-nested-with-required-field")
                .build();
        RequestBody body;
        try {
            body = RequestBody.create(
                    ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        Request okhttpRequest = new Request.Builder()
                .url(httpUrl)
                .method("POST", body)
                .headers(Headers.of(clientOptions.headers(requestOptions)))
                .addHeader("Content-Type", "application/json")
                .build();
        try {
            Response response =
                    clientOptions.httpClient().newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return ObjectMappers.JSON_MAPPER.readValue(
                        response.body().string(), NestedObjectWithRequiredField.class);
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public NestedObjectWithRequiredField getAndReturnNestedWithRequiredField(NestedObjectWithRequiredField request) {
        return getAndReturnNestedWithRequiredField(request, null);
    }
}
