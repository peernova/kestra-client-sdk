package io.kestra.sdk.internal;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;
import com.fasterxml.jackson.databind.node.ArrayNode;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class StringOrArrayDeserializer extends JsonDeserializer<List<String>> {

    @Override
    public List<String> deserialize(JsonParser jsonParser, DeserializationContext deserializationContext) throws IOException {
        var codec = jsonParser.getCodec();
        var node = codec.readTree(jsonParser);

        List<String> result = new ArrayList<>();

        if (node.isArray()) {
            var arrayNode = (ArrayNode) node;

            arrayNode.forEach(item -> result.add(item.asText()));
        } else {
            result.add(node.toString());
        }

        return result;
    }

}
