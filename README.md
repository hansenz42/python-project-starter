# 一个轻量、实用的 Python 项目框架

本项目是一个轻量实用的 Python 项目脚手架，集成了简单的日志，配置文件管理，处理了 python 脚本间的依赖关系，避免重复导入等问题。适用于各种 Python 项目（例如数据科学，web 服务器等）。

项目配置完毕后，你只需要在 src 目录下写代码即可。

该项目的文章在：[🐍 python项目结构的最佳实践 | 窗棂之梦的知识图谱](https://www.windowdaydreaming.top/2023/06/19/python-project-structure/)

欢迎阅读

# 功能

- 依赖管理：使用 poetry 管理项目依赖
- 日志管理：统一化日志格式，支持正常日志和错误日志的分割，分别输出到 stdout 和 stderr
- 配置文件管理：根据不同环境加载不同配置文件。
- 测试管理：使用 pytest 管理测试用例

# 使用方法

## 1 安装 poetry 依赖管理器：

macOS, Linux, Windows(WSL)：
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

其他平台的 poetry 安装方式见：[Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/#installing-with-the-official-installer)

## 2 clone 本项目到本地
```bash
git clone git@github.com:hansenz42/python_scaffold.git
```

## 3 （可选）修改 poetry 的配置

修改 `pyproject.toml`
```toml
[tool.poetry]
name = "PEOJECT NAME"
# ...
authors = ["YOUR NAME <YOUR-EMAIL@xxx.com>"]

[tool.poetry.dependencies]
python = "^3.11"   #替换为你想使用的 python 版本
```


## 4 切换到项目根目录下，安装依赖，修改项目基本信息
```bash
poetry install
```

## 5 如果你使用 IDEA 系列 IDE （PyCharm）

IDE 打开项目后：

将 src 文件夹配置为源代码根目录：
- 右键 src 文件夹，选择 Mark Directory as -> Sources Root

将 res 文件夹配置为资源文件根目录：
- 右键 res 文件夹，选择 Mark Directory as -> Resources Root

将 test 文件夹配置为测试代码根目录：
- 右键 test 文件夹，选择 Mark Directory as -> Test Sources Root

## 6 添加项目变量

项目变量的配置在 `res` 目录下，默认提供了三个环境：
- `config_dev.yml` 开发环境：在开发时使用
- `config_test.yml` 测试环境：在测试时使用
- `config_prod.yml` 生产环境：在正式环境中使用

变量可以写到对应环境的配置文件中，如开发环境的变量写到， `res/config_dev.yml`。

`config.yml` 文件是所有环境共用的配置，如果在特定环境中配置了相同名称的变量，则会覆盖 `config.yml` 中的配置。

## 7 开始写代码！

- 你自己的代码可以放在 `src` 目录下。
- 测试用例可以统一放在 `test` 目录下。

### 7.1 引入自己写的模块

引入自己编写的模块时，使用 `src` 作为根目录起始的路径，如：
```python
# 例如，在 src/service 目录下写了一个 demo_service.py 文件，在其他文件中引入
# 引入的文件路径不写 src，直接从 service 开始即可
from server.demo_service import foo
```

### 7.2 在代码中引入项目变量

在 `config_xxx.yml` 设置一个项目变量 （xxx 为你要配置的环境）

```yaml
foo: 
  bar: 'test_paramter'
```

可在代码中使用以下方式引入，yaml 中的层级用字符串列表表示：

```python
# 引入 ConfigManager
from component.ConfigManager import config_manager

# 获取 yaml 中配置的变量 foo.bar
try:
    config_str = config_manager.get_value(['foo', 'bar'])
    # > test_paramter
    print(config_str)
except KeyError:
    # 如未找到该变量，抛出 KeyError 异常
    print('foo.bar 不存在')
```

### 7.3 使用日志

在代码中引入日志：

```python
from component.LogManager import log_manager

# 定义一个 Tag
TAG = 'main'

# 使用 Tag 生成一个 logger
log = log_manager.get_logger(TAG)

# 输出日志
log.debug('debug log')
log.info('info log')
log.warning('warning log')
log.error('error log')
```

debug 和 info level 的日志将输出到 stdout，warning 和 error level 的日志将输出到 stderr。

### 7.4 示例

使用了以上功能的示例在 `src/demo.py`。

## 8. 运行

程序将按照顺序指定运行环境： 
1. 环境变量：`PYTHON_SERVICE_ENV` ，如 `PYTHON_SERVICE_ENV=dev poetry run python3 main.py`
2. 命令行实参：如 `poetry run python3 main.py -e dev`

如果程序没有接收到任何参数，或接受了 dev/test/prod 以外的参数，则默认使用 `dev` 环境。

# 高级使用

## 安装依赖
直接用 poetry 安装，会自动修改 `pyproject.toml` 文件

```bash
poetry add <package-name>
```

## 修改日志打印到控制台的输出 Level
在 res 文件夹中配置各个环境的日志输出等级（可选）
```yaml
# 配置为 INFO 级别
log_level: INFO  # 支持 DEBUG, INFO, WARNING, ERROR, CRITICAL 不同等级
```

## 加入更多的运行环境

如果运行环境无法满足你的需求，可以在 `src/common/env.py` 文件中的 `VALID_ENVS` 变量中加入你需要的环境名称。

环境名称加入后，在 `res` 目录下新建一个环境配置文件 yaml


## 写测试

测试文件统一放在 test 目录下，文件名以 `test_` 开头，如 `test_main.py`

# 写在最后

该脚手架是我在写 Python 项目时，为了方便自己管理代码而整理的，如果你有更好的建议，欢迎提 issue 或 PR。
