import os
def writeModel(name):
    
    fileName = "../app/Models/"+name+".php"
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    file = open(fileName, "w") 

    file.write("<?php\n")
    file.write("\n")
    file.write("namespace App\Models;\n")
    file.write("\n")
    file.write("use Illuminate\Database\Eloquent\Factories\HasFactory;\n")
    file.write("use Illuminate\Database\Eloquent\Model;\n")
    file.write("\n")
    file.write("class "+name+" extends Model\n")
    file.write("{\n")
    file.write("    use HasFactory;\n")
    file.write("    protected $fillable = [\n")
    file.write("        'name',\n")
    file.write("        'description',\n")
    file.write("        'state',\n")
    file.write("        'slug',\n")
    file.write("    ];\n")
    file.write("}\n")
    file.close()
