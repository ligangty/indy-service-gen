SECURITY_BINDING_YAML_TEMPLATE="""constraints:
  - role: $ROLE1
    urlPattern: "$URL_PATTERN1"
    methods:
      - POST
      - PUT
      - DELETE
  - role: $ROLE2
    urlPattern: "$URL_PATTERN2"
    methods:
      - POST
      - PUT
      - DELETE
"""