POM_TEMPLATE_CONTENT="""<?xml version="1.0"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <parent>
    <groupId>org.commonjava</groupId>
    <artifactId>service-parent</artifactId>
    <version>2</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <groupId>{{ service.group_id }}</groupId>
  <artifactId>{{ service.artifact_id }}</artifactId>
  <version>1.0.0-SNAPSHOT</version>
  <name>{{ service.name|default(service.artifact_id) }}</name>
  <url>https://github.com/Commonjava/{{ service.repo_name }}</url>
  <description>{{ service.desc|default(service.artifact_id) }}</description>
  <inceptionYear>{{ service.inception_year|default("2023") }}</inceptionYear>

  <scm>
    <connection>scm:git:https://github.com/Commonjava/{{ service.repo_name }}</connection>
    <developerConnection>scm:git:https://github.com/Commonjava/{{ service.repo_name }}</developerConnection>
    <url>https://github.com/Commonjava/{{ service.repo_name }}</url>
    <tag>HEAD</tag>
  </scm>

  <properties>
    <apiVersion>1</apiVersion>
    <projectEmail>https://github.com/Commonjava/{{ service.repo_name }}</projectEmail>

    {% if service.enable_event|default(true) %}
    <eventmodel.version>1.0</eventmodel.version>
    {%- endif %}
    {%- if service.enable_security|default(true) %}
    <indysecurity.verison>1.0</indysecurity.verison>
    {%- endif %}
    
    {%- if service.project_props %}
    <!-- project deps version properties -->
    {% for prop in service.project_props -%}
    <{{prop.name}}>{{prop.value}}</{{prop.name}}>
    {% endfor %}
    <!-- project deps version properties end -->
    {%- endif %}
    
    <skipTests>false</skipTests>
    <plugin.jacoco.skip>false</plugin.jacoco.skip>
  </properties>

  <dependencies>
    {%- if service.enable_event|default(true) %}
    <dependency>
      <groupId>org.commonjava.indy.service</groupId>
      <artifactId>indy-event-model</artifactId>
      <version>${eventmodel.version}</version>
    </dependency>
    {% endif %}
    {%- if service.enable_security|default(true) %}
    <dependency>
      <groupId>org.commonjava.indy.service</groupId>
      <artifactId>indy-security</artifactId>
      <version>${indysecurity.verison}</version>
    </dependency>
    {% endif %}
    <!-- quarkus deps start -->
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-arc</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-resteasy-jackson</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-vertx</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-reactive-routes</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-smallrye-openapi</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-smallrye-context-propagation</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-config-yaml</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-undertow</artifactId>
    </dependency>
    {%- if service.enable_event|default(true) %}
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-smallrye-reactive-messaging-kafka</artifactId>
    </dependency>
    {% endif %}
    {%- if service.enable_security|default(true) %}
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-security</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-keycloak-authorization</artifactId>
    </dependency>
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-oidc</artifactId>
    </dependency>
    {% endif %}

    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-junit5</artifactId>
      <scope>test</scope>
    </dependency>
    {%- if service.enable_security|default(true) %}
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-test-security</artifactId>
      <scope>test</scope>
    </dependency>
    {% endif %}
    <dependency>
      <groupId>io.rest-assured</groupId>
      <artifactId>rest-assured</artifactId>
      <scope>test</scope>
    </dependency>
    {%- if service.enable_event|default(true) %}
    <dependency>
      <groupId>io.smallrye.reactive</groupId>
      <artifactId>smallrye-reactive-messaging-in-memory</artifactId>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.awaitility</groupId>
      <artifactId>awaitility</artifactId>
      <scope>test</scope>
    </dependency>
    {% endif %}
    <!-- quarkus deps end -->
    {%- if service.enable_tracing|default(true) %}
    <!-- quarkus otel deps -->
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-opentelemetry-exporter-otlp</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-api</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-extension-trace-propagators</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-sdk-extension-resources</artifactId>
    </dependency>
    <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-sdk-extension-jaeger-remote-sampler</artifactId>
    </dependency>
    <!-- quarkus otel deps end -->
    {% endif %}
    <dependency>
      <groupId>com.fasterxml.jackson.dataformat</groupId>
      <artifactId>jackson-dataformat-yaml</artifactId>
      <version>2.14.0</version>
    </dependency>
    <dependency>
      <groupId>org.jboss.spec.javax.ws.rs</groupId>
      <artifactId>jboss-jaxrs-api_2.1_spec</artifactId>
      <version>2.0.2.Final</version>
    </dependency>
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.12.0</version>
    </dependency>
    <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpclient</artifactId>
      <version>4.5.13</version>
    </dependency>
    <dependency>
      <groupId>commons-io</groupId>
      <artifactId>commons-io</artifactId>
      <version>2.11.0</version>
    </dependency>
    <dependency>
      <groupId>org.codehaus.plexus</groupId>
      <artifactId>plexus-interpolation</artifactId>
      <version>1.26</version>
    </dependency>
    <dependency>
      <groupId>io.netty</groupId>
      <artifactId>netty-transport-native-epoll</artifactId>
      <classifier>linux-x86_64</classifier>
    </dependency>
  </dependencies>

  <build>
    <resources>
      <resource>
        <directory>src/main/resources</directory>
        <filtering>true</filtering>
      </resource>
    </resources>
    <plugins>
      <plugin>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>${version.plugin.compiler}</version>
        <configuration>
          <forceJavacCompilerUse>true</forceJavacCompilerUse>
        </configuration>
      </plugin>
      <plugin>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-maven-plugin</artifactId>
      </plugin>
      <plugin>
        <groupId>ru.concerteza.buildnumber</groupId>
        <artifactId>maven-jgit-buildnumber-plugin</artifactId>
        <version>1.2.9</version>
        <executions>
          <execution>
            <id>git-buildnumber</id>
            <goals>
              <goal>extract-buildnumber</goal>
            </goals>
            <phase>initialize</phase>
            <configuration>
              <runOnlyAtExecutionRoot>false</runOnlyAtExecutionRoot>
            </configuration>
          </execution>
        </executions>
      </plugin>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>buildnumber-maven-plugin</artifactId>
        <version>1.1</version>
        <executions>
          <execution>
            <id>buildnumbers</id>
            <phase>initialize</phase>
            <goals>
              <goal>create</goal>
            </goals>
            <configuration>
              <timestampFormat>{0,date,yyyy-MM-dd HH:mm Z}</timestampFormat>
            </configuration>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>

</project>
"""