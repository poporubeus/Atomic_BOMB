# Atomic_BOMB
Small codes inspired by the Neutron_diffusion article of Graham written in Python and C++ to learn and improve.

I started from the article [Neutron diffusion - Graham W. Griﬃths](https://www.researchgate.net/publication/323035158_Neutron_diffusion) because it was proposed as an exam by my professor of #Theoretical and Numerical Aspects of Nuclear Physics.
The article shows multiple neutron diffusion events coming from different versions of the same diffusion equation in 2D, 3D, spherical coordinates, or by applying boundaries conditions such as Dirchlet, Von Neumann and so on... It is very nice because the mathematical part is explained so well and, for each experiment there is a small implementation in Maple programming language, so it's not so difficult to "translate" it in Python. I've tried to make it complex by computing the main parts of each diffusion equations (solving an integral) with the programming language I consider a curse......: C++!

For now I've just implemented the Dirchlet conditions and, when I'll have time and I'll be inspired I'll implement all the others. The next idea could be implementing either the integrals in Python and see the speed computations between Python and C++; for now check what I've done and you are very encouraged to give me some tips or to make the code better!
