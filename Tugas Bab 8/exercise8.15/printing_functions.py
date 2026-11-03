def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        design = unprinted_designs.pop()
        print(f"Mencetak model: {design}")
        completed_models.append(design)

def show_completed_models(completed_models):
    print("\nModel yang sudah dicetak:")
    for model in completed_models:
        print(f"  - {model}")