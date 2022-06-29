<?php
namespace App\Http\Livewire\Beneficiary;
use App\Models\Beneficiary;use Livewire\Component;use Illuminate\Support\Str;
use Jantinnerezo\LivewireAlert\LivewireAlert;

class BeneficiaryCreate extends Component
{
    use LivewireAlert;
    public $name;
    public $description;
    public $slug;
    public $state = "ACTIVE";
    public function render()
    {
        return view('livewire.beneficiary.beneficiary-create');
    }
    protected $rules = [
        'name' => 'required|max:100|min:2',
        'description' => 'nullable|max:100|min:2',
        'state' => 'required',
    ];
    public function submit()
    {
        $this->validate();
        Beneficiary::create([
            'name' => $this->name,
            'description' => $this->description,
            'slug' => Str::uuid(),
            'state' => $this->state,
        ]);
        $this->cleanInputs();
        $this->confirm('Registro creado correctamente', [
            'icon' => 'success',
            'toast' => false,
            'position' => 'center',
            'showConfirmButton' => true,
            'showCancelButton' => false,
            'cancelButtonText' => 'Cancelar',
            'confirmButtonText' => 'Aceptar',
            'onConfirmed' => 'confirmed',
        ]);
    }
    public function cleanInputs()
    {
        $this->name = "";
        $this->description = "";
        $this->state = "ACTIVE";
    }
    protected $listeners = [
        'confirmed',
    ];
    public function confirmed()
    {
        return redirect()->route('beneficiary.dashboard');
    }
}
}
