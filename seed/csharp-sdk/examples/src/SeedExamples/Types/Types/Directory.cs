using System.Text.Json.Serialization;
using SeedExamples;

namespace SeedExamples;

public class Directory
{
    [JsonPropertyName("name")]
    public string Name { get; init; }

    [JsonPropertyName("files")]
    public List<List<List<File>>?> Files { get; init; }

    [JsonPropertyName("directories")]
    public List<List<List<Directory>>?> Directories { get; init; }
}