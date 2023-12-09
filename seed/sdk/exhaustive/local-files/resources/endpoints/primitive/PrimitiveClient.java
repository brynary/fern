/**
 * This file was auto-generated by Fern from our API Definition.
 */

package com.fern.sdk.resources.endpoints.primitive;

import com.fern.sdk.core.ApiError;
import com.fern.sdk.core.ClientOptions;
import com.fern.sdk.core.MediaTypes;
import com.fern.sdk.core.ObjectMappers;
import com.fern.sdk.core.RequestOptions;
import java.io.IOException;
import java.lang.Exception;
import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import java.time.OffsetDateTime;
import java.util.UUID;
import okhttp3.Headers;
import okhttp3.HttpUrl;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class PrimitiveClient {
  protected final ClientOptions clientOptions;

  public PrimitiveClient(ClientOptions clientOptions) {
    this.clientOptions = clientOptions;
  }

  public String getAndReturnString(String request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("string")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), String.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public String getAndReturnString(String request) {
    return getAndReturnString(request,null);
  }

  public int getAndReturnInt(int request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("integer")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), int.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public int getAndReturnInt(int request) {
    return getAndReturnInt(request,null);
  }

  public long getAndReturnLong(long request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("long")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), long.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public long getAndReturnLong(long request) {
    return getAndReturnLong(request,null);
  }

  public double getAndReturnDouble(double request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("double")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), double.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public double getAndReturnDouble(double request) {
    return getAndReturnDouble(request,null);
  }

  public boolean getAndReturnBool(boolean request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("boolean")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), boolean.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public boolean getAndReturnBool(boolean request) {
    return getAndReturnBool(request,null);
  }

  public OffsetDateTime getAndReturnDatetime(OffsetDateTime request,
      RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("datetime")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), OffsetDateTime.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public OffsetDateTime getAndReturnDatetime(OffsetDateTime request) {
    return getAndReturnDatetime(request,null);
  }

  public String getAndReturnDate(String request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("date")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), String.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public String getAndReturnDate(String request) {
    return getAndReturnDate(request,null);
  }

  public UUID getAndReturnUuid(UUID request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("uuid")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), UUID.class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public UUID getAndReturnUuid(UUID request) {
    return getAndReturnUuid(request,null);
  }

  public byte[] getAndReturnBase64(byte[] request, RequestOptions requestOptions) {
    HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl()).newBuilder()
      .addPathSegments("primitive")
      .addPathSegments("base64")
      .build();
    RequestBody body;
    try {
      body = RequestBody.create(ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
    }
    catch(Exception e) {
      throw new RuntimeException(e);
    }
    Request okhttpRequest = new Request.Builder()
      .url(httpUrl)
      .method("POST", body)
      .headers(Headers.of(clientOptions.headers(requestOptions)))
      .addHeader("Content-Type", "application/json")
      .build();
    try {
      Response response = clientOptions.httpClient().newCall(okhttpRequest).execute();
      if (response.isSuccessful()) {
        return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), byte[].class);
      }
      throw new ApiError(response.code(), ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public byte[] getAndReturnBase64(byte[] request) {
    return getAndReturnBase64(request,null);
  }
}
