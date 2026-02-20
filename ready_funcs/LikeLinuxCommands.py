import click
import shlex

@click.group()
def cli():
    pass



# настроек очень много, посмотри все
@cli.command()
@click.option('-u', '--user_id', type=int, help='ID пользователя')
@click.option('-r', '--recursive', is_flag=True, help='Рекурсивно')
@click.argument('category', help="123")
def stats(user_id, recursive, category):
    print(f"Выполняю STATS: пользователь={user_id}, рекурсия={recursive}, категория={category}")

def run_my_string(command_string):
    # 1. Превращаем строку в список (как в терминале)
    # Пример: 'stats -u 111 --recursive messages' 
    # -> ['stats', '-u', '111', '--recursive', 'messages']
    tokens = shlex.split(command_string)
    
    try:
        # 2. Вызываем Click вручную
        # standalone_mode=False предотвращает sys.exit() при ошибках
        cli.main(args=tokens, standalone_mode=False)
    except click.ClickException as e:
        print(f"Ошибка команды: {e}")
    except Exception as e:
        print(f"Что-то пошло не так: {e}")

# Тест:
run_my_string('stats --help')