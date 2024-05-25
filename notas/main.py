import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('notas.csv', sep=',')

nota_maxima_submodulo = df[['Primer Submodulo', 'Segundo Submodulo', 'Tercer Submodulo', 'Cuarto Submodulo']].max()

print("Nota maxima por submodulo")
print(nota_maxima_submodulo)

nota_minima_submodulo = df[['Primer Submodulo', 'Segundo Submodulo', 'Tercer Submodulo', 'Cuarto Submodulo']].min()

print("Nota minima por submodulo")
print(nota_minima_submodulo)

nota_media = df[['Primer Submodulo', 'Segundo Submodulo', 'Tercer Submodulo', 'Cuarto Submodulo']].mean()

print("Media notas por submodulo")
print(nota_media)


df['Nota Maxima'] = df[['Primer Submodulo', 'Segundo Submodulo', 'Tercer Submodulo', 'Cuarto Submodulo']].max(axis=1)
df['Nota Minima'] = df[['Primer Submodulo', 'Segundo Submodulo', 'Tercer Submodulo', 'Cuarto Submodulo']].min(axis=1)
df['Media'] = df[['Primer Submodulo', 'Segundo Submodulo', 'Tercer Submodulo', 'Cuarto Submodulo']].mean(axis=1)
print(df)


plt.figure(figsize=(10,5))
plt.bar(df['Estudiante'], df['Nota Maxima'])
plt.title('Nota Maxima')
plt.xlabel('Estudiante')
plt.ylabel('Nota Maxima')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10,5))
plt.bar(df['Estudiante'], df['Nota Minima'])
plt.title('Nota Minima')
plt.xlabel('Estudiante')
plt.ylabel('Nota Minima')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10,5))
plt.bar(df['Estudiante'], df['Media'])
plt.title('Nota Media')
plt.xlabel('Estudiante')
plt.ylabel('Nota Media')
plt.xticks(rotation=45)
plt.show()



plt.figure(figsize=(10,5))
plt.pie(df['Nota Maxima'], labels=df['Estudiante'])
plt.title('Nota Maxima')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
plt.pie(df['Nota Minima'], labels=df['Estudiante'])
plt.title('Nota Minima')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
plt.pie(df['Media'], labels=df['Estudiante'])
plt.title('Media')
plt.xticks(rotation=45)
plt.show()