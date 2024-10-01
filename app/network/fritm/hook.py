from pathlib import Path

import frida

SCRIPT = (Path(__file__).parent / "script.js").read_text()


def spawn_and_hook(program, port=8080, filter="true"):
    pid = frida.spawn(program)
    hook(pid, port, filter)
    frida.resume(pid)


def hook(target, port=8080, filter="true"):
    session = frida.attach(target)
    script = SCRIPT.replace("PORT", str(port)).replace("FILTER", filter)
    frida_script = session.create_script(script)
    frida_script.load()
