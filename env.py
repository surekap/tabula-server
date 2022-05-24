#!/usr/bin/env python3

from string import Template
import credstash
import functools

prefix = "metabase"

@functools.lru_cache(maxsize=128)
def getSecret(key):
    secrets = credstash.getAllSecrets()
    return secrets[key]

def main():
    env = Template(open('env.template').read())
    global prefix

    variables = {}
    for m in env.pattern.findall(env.template):
        variables[m[1]] = credstash.getSecret(prefix + "." + m[1])

    print(env.substitute(**variables))

if __name__ == "__main__":
    main()

