# =========================
# Analyse simple ADN
# =========================

# Séquence exemple
sequence = "ATGCTTCAGAAAGGTCTTACG"
sequence = sequence.upper()   # Sécurité : tout en majuscule

# -------------------------
# 1️⃣ Comptage des nucléotides
# -------------------------

def compter_nucleotides(seq):
    compteur = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0
    }

    for base in seq:
        if base in compteur:
            compteur[base] += 1

    return compteur


resultat = compter_nucleotides(sequence)

print("=== Comptage des nucléotides ===")
for base in resultat:
    print(f"{base} : {resultat[base]}")

# -------------------------
# 2️⃣ Calcul du GC Content
# -------------------------

def calcul_gc(seq):
    nb_G = seq.count("G")
    nb_C = seq.count("C")
    longueur = len(seq)

    gc = ((nb_G + nb_C) / longueur) * 100
    return round(gc, 2)


gc_content = calcul_gc(sequence)
print("\n=== GC Content ===")
print(f"Pourcentage GC : {gc_content} %")

# -------------------------
# 3️⃣ Séquence complémentaire
# -------------------------

def complementaire(seq):
    base_comp = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    nouvelle_seq = ""

    for base in seq:
        nouvelle_seq += base_comp[base]

    return nouvelle_seq


seq_comp = complementaire(sequence)
print("\n=== Séquence complémentaire ===")
print(seq_comp)

# -------------------------
# 4️⃣ Reverse complement
# -------------------------

def reverse_complement(seq):
    comp = complementaire(seq)
    return comp[::-1]


rev_comp = reverse_complement(sequence)
print("\n=== Reverse Complement ===")
print(rev_comp)

# -------------------------
# 5️⃣ Recherche d’un motif
# -------------------------

motif = input("\nEntrez un motif à rechercher : ").upper()

nombre = sequence.count(motif)

print(f"Le motif '{motif}' apparaît {nombre} fois.")
