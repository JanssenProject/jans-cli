[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a0f9313eeef046c8810e153a6b7b4ff5)](https://www.codacy.com/gh/JanssenProject/jans-cli/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JanssenProject/jans-cli&amp;utm_campaign=Badge_Grade)

# _Janssen Command Line Interface_
`jans-cli` is a **Command Line Interface** for Janssen Configuration. It also has `menu-driven` interface that makes it easier to understand how to use [Janssen Server](https://github.com/JanssenProject/home) through the Interactive Mode.

# _Installation_

**jans-cli** is automatically installed if you choose `jans-config-api` during installation 
of the [Janssen Server](https://github.com/JanssenProject/home).

![](docs/img/jans-config-api.png)

After successfully installed Janssen Server, you will get two command-line arguments as below:

![](docs/img/installed.png)

# _Quick Start_

As you have seen, CLI supports both of the `config-cli` and `scim-cli`. For a quick start, let's run the following command.

```
/opt/jans/jans-cli/config-cli.py
```
If you get an error, you can try in this way:

```
python3 /opt/jans/jans-cli/config-cli.py
```

Alternatively, you can make python3 to default version:
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
/opt/jans/jans-cli/config-cli.py
```

You will get a menu as below image:

![main-menu.png](docs/img/im-main.png)

From the following list, you can choose any options by selecting its number. For example, let's say number 2,
to get **Default Authentication Method**.

That returns another two options as below:

![option-2-option.png](docs/img/im-default-auth-02.png)

Now selecting 1 and it returns our desired result as below image:

![default-authentication-method.png](docs/img/im-cur-default-auth.png)

So, That was a quick start to view how this `_jans-cli_` Interactive Mode works. Please, follow this [link](docs) to read the `_jans-cli_` docs for a better understanding of the Janssen Command-Line.
