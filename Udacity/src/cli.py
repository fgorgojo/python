import subprocess
import random

# No funciona en Windows: sí en el linux de Udacity.
#call = subprocess.call(['emoj','dog'])

# Solución para windows:
# shell=True permite que Windows resuelva emoj
#Este es correcto para CLIs externos
#subprocess.run("emoj dog", shell=True, check=True)

# Otra forma . Le añadimos el shell=True , pero NO el check=True
# p = subprocess.Popen(['emoj','dog'],shell=True,  stdout=subprocess.PIPE)
# output, err = p.communicate()
# p_status = p.wait()

# print(output)  # b'\xf0\x9f\x90\xb6  \xf0\x9f\x90\xa9  \xf0\x9f\x90\xbe\n'
# print(output.decode('utf-8'))

# emoji = output.decode('utf-8').split(' ')
# emoji_clean = [e for e in emoji if e.strip() != '' ]
# print(random.choice(emoji_clean))


p = subprocess.run(['emoj', 'dog'],shell=True, stdout=subprocess.PIPE)
emoji = p.stdout.decode('utf-8').split(' ')
print(random.choice(emoji))
emoji_clean = [e for e in emoji if e.strip() != '' ]
print(emoji_clean)




