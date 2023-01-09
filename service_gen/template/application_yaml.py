APPLICATION_YAML_TEMPLATE="""quarkus:
  http:
    port: 8080
    read-timeout: 30m
    limits:
      max-body-size: 500M
  package:
    type: uber-jar
  application:
    name: "{{ service.name }}"
  resteasy:
    gzip:
      enabled: true
      max-input: 64M
  {%- if service.enable_security|default(true) %}
  keycloak:
    devservices:
      enabled: false
  oidc:
    enabled: false
  security:
    auth:
      enabled-in-dev-mode: false
  {%- endif %}
  log:
    level: INFO
    min-level: TRACE
    category:
      "org.jboss":
        level: WARN
      "org.apache.kafka":
        level: WARN
      "io.quarkus":
        level: WARN
      "io.smallrye":
        level: WARN
      "org.eclipse":
        level: WARN
      "io.netty":
        level: WARN
      "org.commonjava.indy.service":
        level: TRACE
    console:
      enable: true
      level: DEBUG
    file:
      level: DEBUG
      enable: true
      path: "log/{{ service.name }}.log"
      format: "%d{HH:mm:ss} %-5p [%c{2.}] (%t) %s%e%n"
      rotation:
        max-backup-index: 5
        max-file-size: 10M
  swagger-ui:
    always-include: true
  opentelemetry:
    enabled: false

{%- if service.enable_event|default(true) %}
kafka:
  bootstrap:
    servers: "localhost:9092"

mp:
  messaging:
    emitter:
      # the default buffer size for emitter's OnOverflow buffer strategy of back-pressure control
      default-buffer-size: 1024
    outgoing:
      store-event:
        connector: "smallrye-kafka"
        topics: "Please change your topics here"
        value:
          serializer: "io.quarkus.kafka.client.serialization.ObjectMapperSerializer"
{% endif %}

{%- if service.enable_security|default(true) %}
indy_security:
  enabled: True
{% endif %}

"%dev":
  quarkus:
    log:
      level: TRACE
      min-level: TRACE
      category:
        "org.jboss":
          level: INFO
        "org.apache.kafka":
          level: ERROR
        "io.quarkus":
          level: INFO
        "io.smallrye":
          level: INFO
        "org.eclipse":
          level: INFO
        "io.netty":
          level: INFO
        "org.commonjava.indy.service":
          level: TRACE
      console:
        enable: true
      file:
        enable: true
        path: "/tmp/{{ service.name }}.log"
        format: "%d{HH:mm:ss} %-5p [%c{2.}] (%t) %s%e%n"
        rotation:
          max-backup-index: 5
          max-file-size: 10M
"""