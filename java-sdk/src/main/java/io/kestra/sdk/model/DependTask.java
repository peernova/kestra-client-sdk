package io.kestra.sdk.model;

import lombok.Data;

import java.util.List;

@Data
public class DependTask {

    private Task task;
    private List<String> dependsOn;

}
