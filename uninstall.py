import argparse
import configparser
import glob
import os
import shutil
from helpers import mergepacks
from helpers import mergerstb

args = None

def main():
    i = 0
    mods = {}
    for rulef in glob.iglob(os.path.join(args.directory, 'BotwMod*/rules.txt')):
        rules = configparser.ConfigParser()
        rules.read(rulef)
        mods[i] = {
            'name' : rules['Definition']['name'],
            'priority' : rules['Definition']['fsPriority'],
            'path' : os.path.dirname(rulef)
        }
        if mods[i]['name'] == 'BCML': continue
        print(f'{i + 1}. {mods[i]["name"]} — Priority: {mods[i]["priority"]}')
        i += 1
    
    target = '9999'
    while int(target) - 1 not in mods:
        target = input('Enter the number of the mod you would like to uninstall: ')
    modtarget = mods[int(target) - 1]
    remerge = os.path.exists(os.path.join(modtarget['path'], 'packs.log'))
    try:
        shutil.rmtree(modtarget['path'])
        mergerstb.main(args.directory, "verb" if args.verbose else "quiet")
        if remerge: mergepacks.main(args.directory, args.verbose)
        print('Mod uninstalled successfully')
    except Exception as e:
        print(f'There was an error uninstalling {modtarget["name"]}')
        print('Check error.log for details')
        with open('error.log','w') as elog:
            elog.write(e.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Uninstaller for BCML-managed mods')
    parser.add_argument('-d', '--directory', help = 'Specify path to Cemu graphicPacks folder, default assumes relative path from BCML install directory', default = '../graphicPacks', type = str)
    parser.add_argument('-v', '--verbose', help = 'Verbose output covering every file processed', action='store_true')
    args = parser.parse_args()
    main()