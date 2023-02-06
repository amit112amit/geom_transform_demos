"""
Projective Transformations
"""
from numpy import array, cos, eye, pi, sin


def rotation(θ=0.0):
    """
    Rotation matrix for 2D rotation about z-axis.
    
    Parameters:
    -----------
    θ: angle of rotation about the z-axis.
    
    Output:
    -------
    R: 2x2 rotation matrix
    """
    R = array([[cos(θ), -sin(θ)],
               [sin(θ),  cos(θ)]])
    return R


def affinematrix(θ=0.0, φ=0.0, λ1=1.0, λ2=1.0):
    """
    Create a 2x2 affine matrix from scalings and rotations.

    Parameters:
    -----------
    θ: final rotation
    φ: orientation for scaling
    λ1: scaling in the rotated x direction.
    λ2: scaling in the rotated y direction.

    Output:
    -------
    A: 2x2 affine matrix
    """
    Rθ = rotation(θ)
    Rφ = rotation(φ)
    Rφi = rotation(-φ)
    D = array([[λ1, 0.0], [0.0, λ2]]) 
    A = Rθ @ Rφi @ D @ Rφ
    return A


def affinity(A=eye(2), tx=0.0, ty=0.0):
    """
    Affine transformation.
    
    Parameters:
    -----------
    A: a 2 x 2 non-singular matrix.
    tx: translation in the x-direction.
    ty: translation in the y-direction
    
    Output:
    -------
    H: a similarity transformation matrix 
    """
    a11 = A[0, 0]
    a12 = A[0, 1]
    a21 = A[1, 0]
    a22 = A[1, 1]
    H = array([[a11, a12, tx],
               [a21, a22, ty],
               [0.0, 0.0, 1.]])
    return H


def isometry(ε=1, θ=0.0, tx=0.0, ty=0.0):
    """
    Isometric transformation.
    
    Parameters:
    -----------
    ε: +1 for orientation-preserving transform (i.e. rotation)
       -1 for orientation-reversing
    θ: angle of rotation about the origin.
    tx: translation in the x-direction.
    ty: translation in the y-direction
    
    Output:
    -------
    H: an isometric transformation matrix 
    """
    H = array([[ε * cos(θ), -sin(θ),  tx],
               [ε * sin(θ),  cos(θ),  ty],
               [       0.0,     0.0, 1.0]])
    return H


def similarity(s=1.0, θ=0.0, tx=0.0, ty=0.0):
    """
    Similarity transformation.
    
    Parameters:
    -----------
    s: isotropic scaling ratio.
    θ: angle of rotation about the origin.
    tx: translation in the x-direction.
    ty: translation in the y-direction
    
    Output:
    -------
    H: a similarity transformation matrix 
    """
    H = array([[s * cos(θ), -s * sin(θ),  tx],
               [s * sin(θ),  s * cos(θ),  ty],
               [       0.0,         0.0, 1.0]])
    return H


def projectivity(A=eye(2), tx=0, ty=0, v1=0, v2=0, v=1):
    """
    Projective transformation.
    
    Parameters:
    -----------
    A: a non-singular 2x2 matrix.
    tx: translation in the x-direction.
    ty: translation in the y-direction
    v1, v2: control mapping of vanishing points
    v: the (3, 3) element of the transformation matrix
    
    Output:
    -------
    H: a projective transformation matrix 
    """
    a11 = A[0, 0]
    a12 = A[0, 1]
    a21 = A[1, 0]
    a22 = A[1, 1]
    H = array([[a11, a12, tx],
               [a21, a22, ty],
               [ v1,  v2,  v]])
    return H


def projective_submatrix(s=1, R=eye(2), K=eye(2), tx=0, ty=0, v1=0, v2=0):
    """
    Calculate the upper left 2x2 submatrix of a projective transformation.
    """
    return s * (R @ K) + (array([[tx], [ty]]) @ array([[v1, v2]]))