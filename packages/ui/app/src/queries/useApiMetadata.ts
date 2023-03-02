import { Loadable } from "@fern-api/loadable";
import { TypedQueryKey, useTypedQuery } from "@fern-api/react-query-utils";
import { FernRegistry } from "@fern-fern/registry";
import { useRegistryService } from "../services/useRegistryService";

export function useApiMetadata(
    apiId: FernRegistry.ApiId
): Loadable<FernRegistry.ApiMetadata, FernRegistry.registry.getApiMetadata.Error> {
    const registryService = useRegistryService();
    return useTypedQuery<FernRegistry.ApiMetadata, FernRegistry.registry.getApiMetadata.Error>(
        buildQueryKey({ apiId }),
        async () => {
            const response = await registryService.registry.getApiMetadata(FernRegistry.OrgId("fern"), apiId);
            if (response.ok) {
                return response.body;
            } else {
                // eslint-disable-next-line @typescript-eslint/no-throw-literal
                throw response.error;
            }
        }
    );
}

function buildQueryKey({ apiId }: { apiId: FernRegistry.ApiId }): TypedQueryKey<FernRegistry.ApiMetadata> {
    return TypedQueryKey.of(["api", apiId, "metadata"]);
}