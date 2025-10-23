# Read Me First
The following was discovered as part of building this project:

* The original package name 'com.aitudes.spring-ai-starter' is invalid and this project uses 'com.aitudes.spring_ai_starter' instead.

# Getting Started

### Reference Documentation
For further reference, please consider the following sections:

* [Official Gradle documentation](https://docs.gradle.org)
* [Spring Boot Gradle Plugin Reference Guide](https://docs.spring.io/spring-boot/3.4.7/gradle-plugin)
* [Create an OCI image](https://docs.spring.io/spring-boot/3.4.7/gradle-plugin/packaging-oci-image.html)
* [GraalVM Native Image Support](https://docs.spring.io/spring-boot/3.4.7/reference/packaging/native-image/introducing-graalvm-native-images.html)
* [Distributed Tracing Reference Guide](https://docs.micrometer.io/tracing/reference/index.html)
* [Getting Started with Distributed Tracing](https://docs.spring.io/spring-boot/3.4.7/reference/actuator/tracing.html)
* [Spring Boot Testcontainers support](https://docs.spring.io/spring-boot/3.4.7/reference/testing/testcontainers.html#testing.testcontainers)
* [Testcontainers GCloud Module Reference Guide](https://java.testcontainers.org/modules/gcloud/)
* [Testcontainers Postgres Module Reference Guide](https://java.testcontainers.org/modules/databases/postgres/)
* [Testcontainers Chroma Module Reference Guide](https://java.testcontainers.org/modules/testcontainers/)
* [Testcontainers Ollama Module Reference Guide](https://java.testcontainers.org/modules/testcontainers/)
* [Spring Configuration Processor](https://docs.spring.io/spring-boot/3.4.7/specification/configuration-metadata/annotation-processor.html)
* [Spring Boot DevTools](https://docs.spring.io/spring-boot/3.4.7/reference/using/devtools.html)
* [Spring Web](https://docs.spring.io/spring-boot/3.4.7/reference/web/servlet.html)
* [Spring Reactive Web](https://docs.spring.io/spring-boot/3.4.7/reference/web/reactive.html)
* [htmx](https://github.com/wimdeblauwe/htmx-spring-boot)
* [JDBC API](https://docs.spring.io/spring-boot/3.4.7/reference/data/sql.html)
* [Mustache](https://docs.spring.io/spring-boot/3.4.7/reference/web/servlet.html#web.servlet.spring-mvc.template-engines)
* [Spring Data Redis (Access+Driver)](https://docs.spring.io/spring-boot/3.4.7/reference/data/nosql.html#data.nosql.redis)
* [Spring Security](https://docs.spring.io/spring-boot/3.4.7/reference/web/spring-security.html)
* [Spring gRPC](https://docs.spring.io/spring-grpc/reference/index.html)
* [Spring Boot Actuator](https://docs.spring.io/spring-boot/3.4.7/reference/actuator/index.html)
* [OTLP for metrics](https://docs.spring.io/spring-boot/3.4.7/reference/actuator/metrics.html#actuator.metrics.export.otlp)
* [Spring REST Docs](https://docs.spring.io/spring-restdocs/docs/current/reference/htmlsingle/)
* [Testcontainers](https://java.testcontainers.org/)
* [Google Cloud Support](https://googlecloudplatform.github.io/spring-cloud-gcp/reference/html/index.html)
* [Anthropic Claude](https://docs.spring.io/spring-ai/reference/api/chat/anthropic-chat.html)
* [Model Context Protocol Server](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html)
* [OpenAI](https://docs.spring.io/spring-ai/reference/api/chat/openai-chat.html)
* [Model Context Protocol Client](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html)
* [In-memory Chat Memory Repository](https://docs.spring.io/spring-ai/reference/api/chat-memory.html)
* [Markdown Document Reader](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html#_markdown)
* [Docker Compose Support](https://docs.spring.io/spring-boot/3.4.7/reference/features/dev-services.html#features.dev-services.docker-compose)
* [Tika Document Reader](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html#_tika_docx_pptx_html)
* [Timefold Solver](https://timefold.ai/docs/timefold-solver/latest/quickstart/spring-boot/spring-boot-quickstart#springBootJavaQuickStart)
* [PGvector Vector Database](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html)
* [Ollama](https://docs.spring.io/spring-ai/reference/api/chat/ollama-chat.html)
* [JDBC Chat Memory Repository](https://docs.spring.io/spring-ai/reference/api/chat-memory.html)
* [Chroma Vector Database](https://docs.spring.io/spring-ai/reference/api/vectordbs/chroma.html)

### Guides
The following guides illustrate how to use some features concretely:

* [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
* [Serving Web Content with Spring MVC](https://spring.io/guides/gs/serving-web-content/)
* [Building REST services with Spring](https://spring.io/guides/tutorials/rest/)
* [Building a Reactive RESTful Web Service](https://spring.io/guides/gs/reactive-rest-service/)
* [htmx](https://www.youtube.com/watch?v=j-rfPoXe5aE)
* [Accessing Relational Data using JDBC with Spring](https://spring.io/guides/gs/relational-data-access/)
* [Managing Transactions](https://spring.io/guides/gs/managing-transactions/)
* [Messaging with Redis](https://spring.io/guides/gs/messaging-redis/)
* [Securing a Web Application](https://spring.io/guides/gs/securing-web/)
* [Spring Boot and OAuth2](https://spring.io/guides/tutorials/spring-boot-oauth2/)
* [Authenticating a User with LDAP](https://spring.io/guides/gs/authenticating-ldap/)
* [Building a RESTful Web Service with Spring Boot Actuator](https://spring.io/guides/gs/actuator-service/)
* [Google Cloud Samples](https://github.com/GoogleCloudPlatform/spring-cloud-gcp/tree/main/spring-cloud-gcp-samples)

### Additional Links
These additional references should also help you:

* [Gradle Build Scans – insights for your project's build](https://scans.gradle.com#gradle)
* [Configure AOT settings in Build Plugin](https://docs.spring.io/spring-boot/3.4.7/how-to/aot.html)
* [Various sample apps using Spring gRPC](https://github.com/spring-projects/spring-grpc/tree/main/samples)
* [Timetabling sample. Assign lessons to timeslots and rooms to produce a better schedule for teachers and students](https://github.com/TimefoldAI/timefold-quickstarts/tree/stable/java/spring-boot-integration)

### Docker Compose support
This project contains a Docker Compose file named `compose.yaml`.
In this file, the following services have been defined:

* chroma: [`chromadb/chroma:latest`](https://hub.docker.com/r/chromadb/chroma)
* ollama: [`ollama/ollama:latest`](https://hub.docker.com/r/ollama/ollama)
* pgvector: [`pgvector/pgvector:pg16`](https://hub.docker.com/r/pgvector/pgvector)
* redis: [`redis:latest`](https://hub.docker.com/_/redis)

Please review the tags of the used images and set them to the same as you're running in production.

## GraalVM Native Support

This project has been configured to let you generate either a lightweight container or a native executable.
It is also possible to run your tests in a native image.

### Lightweight Container with Cloud Native Buildpacks
If you're already familiar with Spring Boot container images support, this is the easiest way to get started.
Docker should be installed and configured on your machine prior to creating the image.

To create the image, run the following goal:

```
$ ./gradlew bootBuildImage
```

Then, you can run the app like any other container:

```
$ docker run --rm -p 8080:8080 spring-ai-starter:0.0.1-SNAPSHOT
```

### Executable with Native Build Tools
Use this option if you want to explore more options such as running your tests in a native image.
The GraalVM `native-image` compiler should be installed and configured on your machine.

NOTE: GraalVM 22.3+ is required.

To create the executable, run the following goal:

```
$ ./gradlew nativeCompile
```

Then, you can run the app as follows:
```
$ build/native/nativeCompile/spring-ai-starter
```

You can also run your existing tests suite in a native image.
This is an efficient way to validate the compatibility of your application.

To run your existing tests in a native image, run the following goal:

```
$ ./gradlew nativeTest
```

### Gradle Toolchain support

There are some limitations regarding Native Build Tools and Gradle toolchains.
Native Build Tools disable toolchain support by default.
Effectively, native image compilation is done with the JDK used to execute Gradle.
You can read more about [toolchain support in the Native Build Tools here](https://graalvm.github.io/native-build-tools/latest/gradle-plugin.html#configuration-toolchains).

### Testcontainers support

This project uses [Testcontainers at development time](https://docs.spring.io/spring-boot/3.4.7/reference/features/dev-services.html#features.dev-services.testcontainers).

Testcontainers has been configured to use the following Docker images:

* [`chromadb/chroma:latest`](https://hub.docker.com/r/chromadb/chroma)
* [`ollama/ollama:latest`](https://hub.docker.com/r/ollama/ollama)
* [`pgvector/pgvector:pg16`](https://hub.docker.com/r/pgvector/pgvector)
* [`postgres:latest`](https://hub.docker.com/_/postgres)
* [`redis:latest`](https://hub.docker.com/_/redis)

Please review the tags of the used images and set them to the same as you're running in production.
