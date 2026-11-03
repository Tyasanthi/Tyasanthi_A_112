def make_sandwich(*items):
    print("\nMembuat sandwich dengan isian:")
    for item in items:
        print(f"  - {item}")

make_sandwich("keju")
make_sandwich("ham", "keju", "tomat")
make_sandwich("tuna", "selada", "bawang", "mayones", "acar")