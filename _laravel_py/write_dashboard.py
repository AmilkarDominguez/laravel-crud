import os
def writeDashboard(name, nameView):

    fileName = "../app/Http/Livewire/"+name+"/"+name+"Dashboard.php"
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    file = open(fileName, "w")

    file.write("<?php\n")
    file.write("\n")
    file.write("namespace App\Http\Livewire\\"+name+";\n")
    file.write("\n")
    file.write("use Livewire\Component;\n")
    file.write("class "+name+"Dashboard extends Component\n")
    file.write("{\n")
    file.write("public function render()\n")
    file.write("   {\n")
    file.write("       return view('livewire."+nameView+"."+nameView+"-dashboard');\n")
    file.write("   }\n")
    file.write("}\n")
    file.close()
