import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

direct_path_static = "./static"
direct_path_public = "./docs"
direct_path_content = "./content"
template_path = "./template.html"
template_path_2 = "./template2.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("Deleting public directory...")
    if os.path.exists(direct_path_public):
        shutil.rmtree(direct_path_public)
    print("Copying static files to public directory...")
    copy_files_recursive(direct_path_static, direct_path_public)
    print("Generating page...")
    generate_pages_recursive(direct_path_content, template_path, direct_path_public, basepath)
    generate_page(
        os.path.join(direct_path_content, "pokemon/bulbasaur/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/bulbasaur/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/charmander/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/charmander/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/squirtle/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/squirtle/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/caterpie/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/caterpie/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/weedle/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/weedle/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/pidgey/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/pidgey/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/rattata/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/rattata/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/spearow/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/spearow/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/ekans/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/ekans/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/sandshrew/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/sandshrew/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/nidoranf/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/nidoranf/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/nidoranm/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/nidoranm/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/vulpix/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/vulpix/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/zubat/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/zubat/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/oddish/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/oddish/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/paras/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/paras/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/venonat/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/venonat/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/diglett/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/diglett/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/meowth/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/meowth/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/psyduck/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/psyduck/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/mankey/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/mankey/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/growlithe/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/growlithe/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/poliwag/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/poliwag/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/abra/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/abra/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/machop/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/machop/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/bellsprout/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/bellsprout/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/tentacool/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/tentacool/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/geodude/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/geodude/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/ponyta/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/ponyta/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/slowpoke/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/slowpoke/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/magnemite/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/magnemite/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/farfetchd/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/farfetchd/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/doduo/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/doduo/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/seel/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/seel/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/grimer/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/grimer/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/shellder/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/shellder/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/gastly/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/gastly/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/onix/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/onix/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/drowzee/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/drowzee/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/krabby/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/krabby/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/voltorb/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/voltorb/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/exeggcute/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/exeggcute/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/cubone/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/cubone/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/lickitung/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/lickitung/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/koffing/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/koffing/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/rhyhorn/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/rhyhorn/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/tangela/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/tangela/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/kangaskhan/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/kangaskhan/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/horsea/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/horsea/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/goldeen/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/goldeen/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/staryu/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/staryu/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/scyther/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/scyther/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/pinsir/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/pinsir/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/tauros/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/tauros/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/magikarp/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/magikarp/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/lapras/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/lapras/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/ditto/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/ditto/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/eevee/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/eevee/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/porygon/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/porygon/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/omanyte/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/omanyte/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/kabuto/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/kabuto/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/aerodactyl/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/aerodactyl/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/dratini/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/dratini/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/pikachu/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/pikachu/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/clefairy/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/clefairy/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/jigglypuff/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/jigglypuff/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/hitmonlee/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/hitmonlee/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/hitmonchan/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/hitmonchan/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/chansey/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/chansey/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/mrmime/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/mrmime/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/jynx/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/jynx/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/electabuzz/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/electabuzz/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/magmar/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/magmar/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/snorlax/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/snorlax/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/articuno/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/articuno/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/moltres/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/moltres/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/zapdos/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/zapdos/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/mewtwo/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/mewtwo/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/mew/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/mew/index.html"))
    generate_page(
        os.path.join(direct_path_content, "secrets/reasons/index.md"),
        template_path_2,
        os.path.join(direct_path_public, "secrets/reasons/index.html"))

main()
