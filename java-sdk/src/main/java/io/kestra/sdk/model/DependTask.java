package io.kestra.sdk.model;

import lombok.Data;
import lombok.EqualsAndHashCode;

import java.util.List;

@Data
@EqualsAndHashCode(callSuper = true)
public class DependTask extends Task {

    private Task task;

    private List<String> dependsOn;

}
