
import inquirer
from slugify import slugify
from inquirer.themes import GreenPassion


def main():
    basic_info = [
        inquirer.Text(
            "project_name", message="Inserisci il nome del progetto"
        ),
        # {
        #     "type": "input",
        #     "name": "project_app_name",
        #     "message": "Inserisci il nome dell'app del progetto",
        #     "validate": StringValidator,
        #     "filter": lambda val: str(val)
        # },
        # {
        #     "type": "input",
        #     "name": "project_app_name",
        #     "message": "Inserisci il nome utilizzato per i docker hostname",
        #     "validate": StringValidator,
        #     "filter": lambda val: str(val)
        # },
    ]
    answers = inquirer.prompt(basic_info)
    print(f"{answers=}")
    second_step_questions = [
        inquirer.Text(
            "project_dirname",
            message="Inserisci il nome della cartella di progetto",
            default=slugify(answers.get("project_name"))
        ),
        inquirer.Checkbox(
            "packages_to_install",
            message="Seleziona i pacchetti che vuoi includere nel nuovo progetto",
            choices=["django-cms", "celery", "celery-beat", "rabbit"]
        )
    ]
    answers_second_step = inquirer.prompt(second_step_questions, theme=GreenPassion())
    print(f"{answers_second_step=}")


if __name__ == "__main__":
    main()
