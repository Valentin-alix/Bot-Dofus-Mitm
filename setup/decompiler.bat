set ffDecJar="C:\Program Files (x86)\FFDec\ffdec.jar"
set dofInvoker="C:\Users\valen\AppData\Local\Ankama\Dofus\DofusInvoker.swf"
set pathDecompile="./scripts_resources"

java -jar %ffDecJar% -selectclass com.ankamagames.dofus.network.messages.++,com.ankamagames.dofus.network.types.++,com.ankamagames.dofus.network.ProtocolTypeManager,com.ankamagames.dofus.network.MessageReceiver -export script %pathDecompile% %dofInvoker%