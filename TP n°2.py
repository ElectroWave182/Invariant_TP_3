def drapeau_hollandais (liste):

    # Initialisation
    n = len (liste)
    b = 0
    w = 0
    r = n - 1

    # Précondition
    for couleur in liste:
        assert couleur == 0 or couleur == 1 or couleur == 2, "0"

    # Invariant
    assert 0 <= b <= w <= r + 1 <= n
    for bleu in liste[: b]:
        assert bleu == 0, "1"
    for blanc in liste[b : w]:
        assert blanc == 1, "2"
    for rouge in liste[r + 1 :]:
        assert rouge == 2, "3"

    while r != w - 1:

        # Invariant
        assert 0 <= b <= w <= r + 1 <= n
        for bleu in liste[: b]:
            assert bleu == 0, "4"
        for blanc in liste[b : w]:
            assert blanc == 1, "5"
        for rouge in liste[r + 1 :]:
            assert rouge == 2, "6"

        # CC
        assert r != w - 1, "7"

        ele = liste[w]

        if ele == 0:
            liste[b] = 0
            liste[w] = 1
            b += 1
            w += 1

        elif ele == 1:
            w += 1

        else:
            liste[w] = liste[r]
            liste[r] = 2
            r -= 1

        # Invariant
        assert 0 <= b <= w <= r + 1 <= n
        for bleu in liste[: b]:
            assert bleu == 0, "8"
        for blanc in liste[b : w]:
            assert blanc == 1, "9"
        for rouge in liste[r + 1 :]:
            assert rouge == 2, "10"

    # Invariant
    assert 0 <= b <= w <= r + 1 <= n
    for bleu in liste[: b]:
        assert bleu == 0, "11"
    for blanc in liste[b : w]:
        assert blanc == 1, "12"
    for rouge in liste[r + 1 :]:
        assert rouge == 2, "13"

    # non CC
    assert r == w - 1, "14"

    return liste

print (drapeau_hollandais ([1, 2, 0, 1, 1, 2, 0]))