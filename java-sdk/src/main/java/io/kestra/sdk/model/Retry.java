package io.kestra.sdk.model;

import lombok.Data;

import java.time.OffsetDateTime;

@Data
public class Retry {

    private String maxDuration;

    private Integer maxAttempts;

    private Integer maxAttempt;

    private String interval;

    private String type;

    private String behavior;

    private Boolean warningOnRetry;

}
