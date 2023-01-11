README_TEMPLATE="""# {{ service.name }}
{{ service.desc }}

## Prerequisite for building
1. jdk11
2. mvn 3.6.2+

## Prerequisite for debugging in local
1. docker 20+
2. docker-compose 1.20+

## Configure 

see [src/main/resources/application.yaml](./src/main/resources/application.yaml) for details


## Try it

There are a few steps to set it up.

1. Build (make sure you use jdk11 and mvn 3.6.2+)
```
$ git clone {{ service.repo_name }}
$ cd {{ service.artifact_id }}
$ mvn clean compile
```
2. Start in debug mode
```
$ mvn quarkus:dev
```

"""