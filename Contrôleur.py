from personne import personne
 class contoleur(personne):
      def _init_ (sef):
         personne. _init_ (self);
     def verifier(self, solde,mt):
       if (solde < mt):
    return 0: # faux pour solde insuffisant
     else:
   return 1:# vrai pour solde superieur au montant
    def _str_(self):
   return "\c controleur \n"+personne. _str_(self)
